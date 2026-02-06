#!/usr/bin/env python3
"""
Taste Engine - Twitter Trend Collector
Tracks fashion/brand mentions in real-time
"""

import json
import subprocess
import datetime
from collections import Counter
import re

# Brands and terms we're tracking
TRACK_TERMS = [
    # Luxury
    "chrome hearts", "rick owens", "balenciaga", "bottega", "margiela",
    "arc'teryx", "arcteryx", "stone island", "moncler",
    
    # Streetwear  
    "supreme", "palace", "stussy", "carhartt", "dickies",
    "brain dead", "online ceramics", "corteiz",
    
    # Footwear
    "sambas", "salomon", "new balance 550", "nb550",
    "jordan 4", "dunk low", "yeezy",
    
    # Trends
    "gorpcore", "blokecore", "quiet luxury", "mob wife",
    "opium aesthetic", "coquette", "dark academia",
    
    # Retailers
    "ssense", "end clothing", "dover street", "kith",
    "stockx", "grailed", "depop"
]

def search_twitter(query, auth_token, ct0):
    """Search Twitter for a term using bird CLI"""
    cmd = [
        "bird", "search", query,
        "--auth-token", auth_token,
        "--ct0", ct0,
        "-n", "10",
        "--json"
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            return json.loads(result.stdout)
        else:
            return []
    except:
        return []

def analyze_trend(tweets):
    """Extract metrics from tweets"""
    total_engagement = 0
    mentions = []
    
    for tweet in tweets:
        engagement = tweet.get('likes', 0) + tweet.get('retweets', 0) * 2
        total_engagement += engagement
        mentions.append({
            'text': tweet.get('text', '')[:100],
            'engagement': engagement,
            'author': tweet.get('author', {}).get('handle', 'unknown')
        })
    
    return {
        'count': len(tweets),
        'total_engagement': total_engagement,
        'avg_engagement': total_engagement / len(tweets) if tweets else 0,
        'top_mention': max(mentions, key=lambda x: x['engagement']) if mentions else None
    }

def main():
    # Twitter creds (from memory)
    AUTH = "0e124ea53bdd9d743362087b4b85294992f4e3c0"
    CT0 = "1880628f5082da99b5c67085a9cbbea6127d3ee115f5ffdef882fa881b339694d6b79a70c7f1721e96f526d42ab2c8d12450cd44744248f1b3efbe95ac30a78c32948f2fd5ddcf0c92e3a07098b6226d"
    
    timestamp = datetime.datetime.now().isoformat()
    results = {
        'timestamp': timestamp,
        'trends': {}
    }
    
    print(f"🔍 Scanning {len(TRACK_TERMS)} terms...")
    
    # Collect data for each term
    for i, term in enumerate(TRACK_TERMS[:5]):  # Start with just 5 to test
        print(f"  [{i+1}/5] Checking: {term}")
        tweets = search_twitter(term, AUTH, CT0)
        
        if tweets:
            analysis = analyze_trend(tweets)
            results['trends'][term] = analysis
            
            if analysis['avg_engagement'] > 100:
                print(f"    🔥 HOT: {analysis['avg_engagement']:.0f} avg engagement")
    
    # Save results
    output_file = f"/home/ubuntu/taste-engine/data/scan_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n✅ Saved to {output_file}")
    
    # Find top trending
    sorted_trends = sorted(
        results['trends'].items(),
        key=lambda x: x[1]['avg_engagement'],
        reverse=True
    )
    
    print("\n📊 TOP TRENDS:")
    for term, data in sorted_trends[:3]:
        print(f"  • {term}: {data['avg_engagement']:.0f} avg engagement")
        if data['top_mention']:
            print(f"    \"{data['top_mention']['text']}...\"")

if __name__ == "__main__":
    main()