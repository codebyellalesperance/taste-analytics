# Taste Engine 📊

Real-time consumer intelligence platform tracking fashion, brands, and culture trends.

## What it does

Tracks trending topics across:
- Fashion aesthetics (mob wife, quiet luxury, gorpcore)
- Luxury brands (Chrome Hearts, Rick Owens, Balenciaga)
- Streetwear (Supreme, Palace, Stussy)
- Footwear (Sambas, Salomon, New Balance)
- DTC brands and product drops

## Current Features

- **Twitter Scanner**: Tracks 38+ terms in real-time
- **Engagement Analytics**: Measures avg engagement per mention
- **Trend Detection**: Identifies rising trends before mainstream
- **Auto Post Generation**: Creates data-driven content for @tasteengine

## Tech Stack

- Python 3
- `bird` CLI for Twitter data
- Google Trends API (coming)
- StockX scraping (coming)

## Usage

```bash
# Run live dashboard
python3 scripts/dashboard.py

# Generate posts from current data
python3 scripts/generate_posts.py

# Collect Twitter data
python3 scripts/collect_twitter.py
```

## Sample Output

```
"Mob Wife Aesthetic" pulling 45 avg engagement per mention. 
25 posts in last hour. The culture is shifting.
```

## Roadmap

- [ ] Add StockX price tracking
- [ ] Google Trends integration
- [ ] TikTok hashtag tracking
- [ ] Web dashboard
- [ ] Automated posting
- [ ] Alert system for trend spikes
- [ ] B2B platform for brands

## YC Application Potential

"Bloomberg Terminal for consumer culture. We tell brands what's going to be cool before it's cool."

---

Built by @tasteengine | Follow for real-time trend updates