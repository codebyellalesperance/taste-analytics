#!/usr/bin/env python3
"""
Taste Engine - Google Trends Collector
Tracks search volume changes
"""

import json
import datetime
import requests
from urllib.parse import quote

def get_google_trends(term):
    """Get Google Trends data (simplified - would use pytrends in production)"""
    # For MVP, we'll use Google's autocomplete as a proxy for trending
    # In production, use pytrends library
    
    url = f"http://suggestqueries.google.com/complete/search?client=firefox&q={quote(term)}"
    
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        suggestions = data[1] if len(data) > 1 else []
        
        return {
            'term': term,
            'related_searches': suggestions[:5],
            'search_volume_indicator': len(suggestions)  # More suggestions = more search volume
        }
    except:
        return None

def main():
    terms = [
        "chrome hearts", "salomon shoes", "mob wife aesthetic",
        "gorpcore", "sambas", "quiet luxury"
    ]
    
    results = {
        'timestamp': datetime.datetime.now().isoformat(),
        'google_trends': {}
    }
    
    print("📈 Checking Google search trends...")
    
    for term in terms:
        print(f"  • {term}...")
        trend_data = get_google_trends(term)
        if trend_data:
            results['google_trends'][term] = trend_data
            
    # Save results
    output_file = f"/home/ubuntu/taste-engine/data/google_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n✅ Saved to {output_file}")

if __name__ == "__main__":
    main()