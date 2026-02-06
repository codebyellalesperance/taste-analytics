#!/usr/bin/env python3
"""
Generate @tasteengine posts from live data
"""

import json
import subprocess
import datetime

def get_live_data():
    """Get fresh Twitter data"""
    AUTH = "0e124ea53bdd9d743362087b4b85294992f4e3c0"
    CT0 = "1880628f5082da99b5c67085a9cbbea6127d3ee115f5ffdef882fa881b339694d6b79a70c7f1721e96f526d42ab2c8d12450cd44744248f1b3efbe95ac30a78c32948f2fd5ddcf0c92e3a07098b6226d"
    
    # Check multiple trending topics
    topics = {
        "fashion": ["mob wife aesthetic", "quiet luxury", "coquette aesthetic", "gorpcore"],
        "brands": ["chrome hearts", "rick owens", "jacquemus", "ganni"],
        "footwear": ["sambas", "salomon xt-6", "onitsuka tiger"],
        "tech": ["AI fashion", "virtual try on", "digital fashion"]
    }
    
    data = {}
    
    for category, terms in topics.items():
        for term in terms[:2]:  # Check 2 per category
            cmd = ["bird", "search", term, "--auth-token", AUTH, "--ct0", CT0, "-n", "30", "--json"]
            
            try:
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
                if result.returncode == 0:
                    tweets = json.loads(result.stdout)
                    
                    engagement = sum(t.get('likeCount', 0) + t.get('retweetCount', 0) * 2 for t in tweets)
                    
                    data[term] = {
                        'category': category,
                        'mentions': len(tweets),
                        'total_engagement': engagement,
                        'avg_engagement': engagement / len(tweets) if tweets else 0
                    }
            except:
                pass
    
    return data

def generate_posts(data):
    """Create posts based on trends"""
    posts = []
    
    # Sort by engagement
    trending = sorted(data.items(), key=lambda x: x[1]['avg_engagement'], reverse=True)
    
    # Post 1: Top trend
    if trending[0][1]['avg_engagement'] > 20:
        term = trending[0][0]
        metrics = trending[0][1]
        posts.append(
            f'"{term.title()}" pulling {metrics["avg_engagement"]:.0f} avg engagement per mention. '
            f'{metrics["mentions"]} posts in last hour. The culture is shifting.'
        )
    
    # Post 2: Comparison
    if len(trending) > 1:
        winner = trending[0][0]
        loser = trending[-1][0]
        ratio = trending[0][1]['avg_engagement'] / (trending[-1][1]['avg_engagement'] or 1)
        if ratio > 5:
            posts.append(
                f'{winner.title()} getting {ratio:.0f}x more engagement than {loser.title()} right now. '
                f'The algorithm has spoken.'
            )
    
    # Post 3: Category insight
    fashion_trends = [(k, v) for k, v in data.items() if v['category'] == 'fashion']
    if fashion_trends:
        top_fashion = sorted(fashion_trends, key=lambda x: x[1]['avg_engagement'], reverse=True)[0]
        posts.append(
            f'Fashion trend update: "{top_fashion[0]}" leading with {top_fashion[1]["mentions"]} mentions. '
            f'Search this term now before it hits mainstream.'
        )
    
    # Post 4: Rising trend (low mentions but high engagement)
    for term, metrics in data.items():
        if metrics['mentions'] < 10 and metrics['avg_engagement'] > 30:
            posts.append(
                f'Early signal: "{term}" only {metrics["mentions"]} mentions but '
                f'{metrics["avg_engagement"]:.0f} avg engagement. This is about to blow.'
            )
            break
    
    return posts

def main():
    print("🤖 TASTE ENGINE POST GENERATOR\n")
    print("Scanning live data...")
    
    data = get_live_data()
    
    print(f"\nAnalyzed {len(data)} terms\n")
    
    posts = generate_posts(data)
    
    print("📝 GENERATED POSTS:\n")
    for i, post in enumerate(posts, 1):
        print(f"{i}. {post}\n")
    
    # Save posts
    with open('/home/ubuntu/taste-engine/output/posts.txt', 'w') as f:
        for post in posts:
            f.write(post + "\n\n")
    
    print(f"Saved {len(posts)} posts to output/posts.txt")

if __name__ == "__main__":
    main()