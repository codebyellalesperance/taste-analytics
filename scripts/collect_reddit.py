#!/usr/bin/env python3
"""
Taste Engine - Reddit Sentiment Analyzer
Tracks fashion discussion across subreddits
"""

import json
import requests
import datetime

def get_reddit_sentiment(term, subreddit="streetwear+fashion+malefashionadvice"):
    """Check Reddit for mentions and sentiment"""
    
    # Reddit's public JSON API (no auth needed for read)
    url = f"https://www.reddit.com/r/{subreddit}/search.json"
    
    params = {
        'q': term,
        'sort': 'new',
        'limit': 25,
        't': 'week'
    }
    
    headers = {'User-Agent': 'TasteEngine/1.0'}
    
    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        data = response.json()
        
        posts = data.get('data', {}).get('children', [])
        
        total_score = sum(p['data']['score'] for p in posts)
        total_comments = sum(p['data']['num_comments'] for p in posts)
        
        # Extract sentiment indicators
        positive_words = ['love', 'fire', 'grail', 'need', 'want', 'cop', 'clean']
        negative_words = ['hate', 'trash', 'mid', 'overrated', 'dead', 'over']
        
        sentiment_score = 0
        for post in posts:
            title = post['data']['title'].lower()
            for word in positive_words:
                if word in title:
                    sentiment_score += 1
            for word in negative_words:
                if word in title:
                    sentiment_score -= 1
        
        return {
            'mentions': len(posts),
            'total_karma': total_score,
            'total_comments': total_comments,
            'avg_karma': total_score / len(posts) if posts else 0,
            'sentiment': 'positive' if sentiment_score > 0 else 'negative' if sentiment_score < 0 else 'neutral'
        }
    except:
        return None

def track_reddit_trends():
    """Monitor key terms across Reddit"""
    
    terms = [
        "chrome hearts",
        "rick owens", 
        "mob wife aesthetic",
        "salomon xt-6",
        "quiet luxury",
        "archive fashion",
        "gorpcore"
    ]
    
    results = {}
    
    print("📊 Scanning Reddit sentiment...\n")
    
    for term in terms:
        sentiment = get_reddit_sentiment(term)
        if sentiment:
            results[term] = sentiment
            print(f"  {term}: {sentiment['mentions']} posts, {sentiment['sentiment']} sentiment")
    
    return results

def main():
    data = track_reddit_trends()
    
    # Find most discussed
    most_discussed = sorted(data.items(), key=lambda x: x[1]['mentions'], reverse=True)[:3]
    
    print("\n🗣️ MOST DISCUSSED ON REDDIT:")
    for term, info in most_discussed:
        print(f"  {term}: {info['mentions']} posts, {info['total_comments']} comments")
    
    # Find positive sentiment
    positive = [(k, v) for k, v in data.items() if v['sentiment'] == 'positive']
    if positive:
        print("\n😊 POSITIVE SENTIMENT:")
        for term, _ in positive:
            print(f"  {term}")
    
    # Save
    with open('/home/ubuntu/taste-engine/data/reddit_latest.json', 'w') as f:
        json.dump({
            'timestamp': datetime.datetime.now().isoformat(),
            'reddit_data': data
        }, f, indent=2)

if __name__ == "__main__":
    main()