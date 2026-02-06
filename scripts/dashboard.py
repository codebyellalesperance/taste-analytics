#!/usr/bin/env python3
"""
Taste Engine - Live Dashboard
Combines all data sources and generates insights
"""

import json
import subprocess
import datetime
from pathlib import Path

def scan_twitter_live():
    """Quick scan of hot terms"""
    AUTH = "0e124ea53bdd9d743362087b4b85294992f4e3c0"
    CT0 = "1880628f5082da99b5c67085a9cbbea6127d3ee115f5ffdef882fa881b339694d6b79a70c7f1721e96f526d42ab2c8d12450cd44744248f1b3efbe95ac30a78c32948f2fd5ddcf0c92e3a07098b6226d"
    
    hot_terms = ["chrome hearts", "salomon", "mob wife aesthetic", "rick owens", "sambas"]
    
    results = []
    
    for term in hot_terms:
        cmd = [
            "bird", "search", term,
            "--auth-token", AUTH,
            "--ct0", CT0,
            "-n", "20",
            "--json"
        ]
        
        try:
            output = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if output.returncode == 0:
                tweets = json.loads(output.stdout)
                
                # Calculate metrics
                total_engagement = sum(
                    t.get('likeCount', 0) + t.get('retweetCount', 0) * 2 
                    for t in tweets
                )
                
                # Find the hottest tweet
                hottest = max(tweets, key=lambda t: t.get('likeCount', 0) + t.get('retweetCount', 0) * 2) if tweets else None
                
                results.append({
                    'term': term,
                    'mentions': len(tweets),
                    'total_engagement': total_engagement,
                    'avg_engagement': total_engagement / len(tweets) if tweets else 0,
                    'hottest_tweet': {
                        'text': hottest.get('text', '')[:100] if hottest else '',
                        'engagement': hottest.get('likeCount', 0) + hottest.get('retweetCount', 0) * 2 if hottest else 0,
                        'author': hottest.get('author', {}).get('username', '') if hottest else ''
                    } if hottest else None
                })
        except:
            pass
    
    return results

def generate_insights(data):
    """Generate actionable insights from data"""
    insights = []
    
    # Sort by average engagement
    trending = sorted(data, key=lambda x: x['avg_engagement'], reverse=True)
    
    if trending[0]['avg_engagement'] > 1000:
        insights.append(f"🔥 {trending[0]['term'].upper()} is exploding - {trending[0]['avg_engagement']:.0f} avg engagement")
    
    # Find emerging trends (high engagement but low mention count)
    for item in data:
        if item['mentions'] < 10 and item['avg_engagement'] > 500:
            insights.append(f"👀 {item['term']} - Low volume but HIGH engagement. Early signal.")
    
    # Compare trends
    if len(trending) > 1:
        if trending[0]['avg_engagement'] > trending[1]['avg_engagement'] * 3:
            insights.append(f"📊 {trending[0]['term']} getting 3x more engagement than {trending[1]['term']}")
    
    return insights

def main():
    print("=" * 60)
    print("TASTE ENGINE - LIVE DASHBOARD")
    print("=" * 60)
    print(f"Scan time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Scan Twitter
    print("📡 Scanning Twitter trends...")
    data = scan_twitter_live()
    
    # Display results
    print("\n📊 CURRENT METRICS:\n")
    for item in sorted(data, key=lambda x: x['avg_engagement'], reverse=True):
        print(f"{item['term']:20} | {item['mentions']:2} mentions | {item['avg_engagement']:6.0f} avg engagement")
        if item['hottest_tweet'] and item['hottest_tweet']['engagement'] > 100:
            print(f"  └─ @{item['hottest_tweet']['author']}: \"{item['hottest_tweet']['text']}...\"")
    
    # Generate insights
    print("\n💡 INSIGHTS:\n")
    insights = generate_insights(data)
    for insight in insights:
        print(f"  {insight}")
    
    # Generate posts for @tasteengine
    print("\n✍️ SUGGESTED POSTS:\n")
    
    top_trend = sorted(data, key=lambda x: x['avg_engagement'], reverse=True)[0]
    if top_trend['avg_engagement'] > 100:
        print(f'1. "{top_trend["term"].title()} seeing {top_trend["avg_engagement"]:.0f} avg engagement on Twitter right now. {top_trend["mentions"]} mentions in last hour."')
    
    # Save to file
    output = {
        'timestamp': datetime.datetime.now().isoformat(),
        'data': data,
        'insights': insights
    }
    
    output_file = f"/home/ubuntu/taste-engine/output/dashboard_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    Path("/home/ubuntu/taste-engine/output").mkdir(exist_ok=True)
    with open(output_file, 'w') as f:
        json.dump(output, f, indent=2)
    
    print(f"\n💾 Dashboard saved to {output_file}")

if __name__ == "__main__":
    main()