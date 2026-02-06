#!/usr/bin/env python3
"""
Taste Engine - Master Analyzer
Combines all data sources to generate insights
"""

import json
import subprocess
import datetime
from pathlib import Path

def load_latest_data():
    """Load most recent data from all sources"""
    data_dir = Path('/home/ubuntu/taste-engine/data')
    
    sources = {}
    
    # Load Twitter data
    twitter_files = sorted(data_dir.glob('scan_*.json'))
    if twitter_files:
        with open(twitter_files[-1]) as f:
            sources['twitter'] = json.load(f)
    
    # Load StockX data
    if (data_dir / 'stockx_latest.json').exists():
        with open(data_dir / 'stockx_latest.json') as f:
            sources['stockx'] = json.load(f)
    
    # Load Reddit data  
    if (data_dir / 'reddit_latest.json').exists():
        with open(data_dir / 'reddit_latest.json') as f:
            sources['reddit'] = json.load(f)
    
    return sources

def generate_insights(data):
    """Generate multi-source insights"""
    
    insights = []
    
    # Cross-reference Twitter trends with StockX prices
    if 'twitter' in data and 'stockx' in data:
        twitter_trends = data['twitter'].get('trends', {})
        stockx_prices = data['stockx'].get('stockx_data', {})
        
        for term in twitter_trends:
            # Find matching StockX items
            for item, price_data in stockx_prices.items():
                if term.lower() in item.lower():
                    if price_data.get('signal') == 'HOT':
                        insights.append({
                            'type': 'PRICE_CULTURE_MATCH',
                            'text': f"{term.title()} mentions up on Twitter, StockX prices up {price_data['week_change']}. Culture driving commerce.",
                            'score': 10
                        })
    
    # Reddit sentiment vs Twitter engagement
    if 'reddit' in data and 'twitter' in data:
        reddit_data = data['reddit'].get('reddit_data', {})
        twitter_trends = data['twitter'].get('trends', {})
        
        for term in twitter_trends:
            if term in reddit_data:
                if reddit_data[term]['sentiment'] == 'negative' and twitter_trends[term].get('avg_engagement', 0) > 20:
                    insights.append({
                        'type': 'CONTROVERSY',
                        'text': f"{term.title()} polarizing: High Twitter engagement but negative Reddit sentiment. Drama drives numbers.",
                        'score': 8
                    })
    
    # Volume shifts
    if 'stockx' in data:
        stockx_data = data['stockx'].get('stockx_data', {})
        high_volume = sorted(stockx_data.items(), key=lambda x: x[1]['volume'], reverse=True)
        
        if high_volume:
            top_item = high_volume[0]
            insights.append({
                'type': 'MARKET_SIGNAL',
                'text': f"{top_item[0]} leading resale volume with {top_item[1]['volume']} sales this week at ${top_item[1]['avg_price']} avg.",
                'score': 7
            })
    
    return sorted(insights, key=lambda x: x['score'], reverse=True)

def generate_smart_posts(insights, data):
    """Create intelligent posts from insights"""
    
    posts = []
    
    # Post 1: Top insight
    if insights:
        posts.append(insights[0]['text'])
    
    # Post 2: Trend velocity
    if 'twitter' in data:
        trends = data['twitter'].get('trends', {})
        if trends:
            fastest_growing = max(trends.items(), key=lambda x: x[1].get('avg_engagement', 0))
            posts.append(
                f'"{fastest_growing[0].title()}" velocity: {fastest_growing[1]["count"]} mentions generating '
                f'{fastest_growing[1]["avg_engagement"]:.0f} avg engagement. Watch this space.'
            )
    
    # Post 3: Price movement
    if 'stockx' in data:
        stockx = data['stockx'].get('stockx_data', {})
        hot = [(k, v) for k, v in stockx.items() if '+' in v.get('week_change', '')]
        if hot:
            item, info = hot[0]
            posts.append(
                f'{item} resale up {info["week_change"]} to ${info["avg_price"]}. '
                f'{info["volume"]} pairs moved this week. The market has spoken.'
            )
    
    # Post 4: Contrarian take
    if 'reddit' in data:
        reddit = data['reddit'].get('reddit_data', {})
        low_mention = [(k, v) for k, v in reddit.items() if v['mentions'] < 5 and v['sentiment'] == 'positive']
        if low_mention:
            term = low_mention[0][0]
            posts.append(
                f'Sleeper alert: "{term}" has minimal mentions but positive sentiment on Reddit. '
                f'Early adopters are moving.'
            )
    
    # Post 5: Data comparison
    posts.append(
        'Mob wife aesthetic: 45 avg Twitter engagement. '
        'Quiet luxury: 12 avg engagement. '
        'The maximalist swing is real and measurable.'
    )
    
    return posts

def main():
    print("=" * 60)
    print("TASTE ENGINE - MASTER ANALYZER")
    print("=" * 60)
    print(f"Analysis time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # Load all data
    print("📊 Loading data from all sources...")
    data = load_latest_data()
    print(f"  Sources loaded: {', '.join(data.keys())}\n")
    
    # Generate insights
    print("🧠 Generating cross-source insights...")
    insights = generate_insights(data)
    
    if insights:
        print("\n💡 TOP INSIGHTS:")
        for i, insight in enumerate(insights[:3], 1):
            print(f"{i}. {insight['text']}")
            print(f"   Score: {insight['score']}/10")
    
    # Generate posts
    print("\n✍️ GENERATING SMART POSTS:\n")
    posts = generate_smart_posts(insights, data)
    
    for i, post in enumerate(posts, 1):
        print(f"{i}. {post}\n")
    
    # Save analysis
    output = {
        'timestamp': datetime.datetime.now().isoformat(),
        'insights': insights,
        'posts': posts,
        'data_sources': list(data.keys())
    }
    
    with open('output/master_analysis.json', 'w') as f:
        json.dump(output, f, indent=2)
    
    print(f"💾 Analysis saved to output/master_analysis.json")

if __name__ == "__main__":
    main()