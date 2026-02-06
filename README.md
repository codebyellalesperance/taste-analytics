# Taste Engine 📊

Real-time consumer intelligence platform tracking fashion, brands, and culture trends.

## What it does

Tracks trending topics across:
- **Social Media**: TikTok hashtags, Twitter engagement, Reddit sentiment
- **Commerce**: StockX resale prices, volume tracking
- **Institutional**: Fashion Week runways, Super Bowl ads, designer moves
- **Fashion aesthetics**: Mob wife, quiet luxury, gorpcore, opiumcore
- **Brands**: Chrome Hearts, Rick Owens, Balenciaga, Arc'teryx
- **Footwear**: Sambas, Salomon, New Balance

## Features

✅ **Multi-Platform Tracking**
- TikTok: Hashtag velocity, sound-to-fashion correlation, creator influence
- Twitter: Real-time engagement metrics, viral moment detection
- Reddit: Sentiment analysis, community validation
- StockX: Resale price movements, volume tracking
- Runway: Fashion Week trends, runway-to-street gap analysis
- Super Bowl: Major ad campaign tracking, brand spend analysis

✅ **Smart Analytics**
- Cross-platform correlation detection
- Trend velocity scoring (0-100)
- Predictive insights ("This will peak in 7-14 days")
- Runway vs reality gap analysis
- Ad spend vs social reality comparison

✅ **Automated Workflows**
- GitHub Actions runs every 3 hours
- Auto-scans all data sources
- Generates data-driven posts
- Auto-posts to Twitter
- Commits updated data to repo

✅ **Data-Driven Posts**
Real insights like:
> "BMW spending $10.5M to revive quiet luxury in the Super Bowl. Trend score: 8/100. The money already wasted."

> "Pattern detected: Fur coats 78% street adoption before Fashion Week validated. Culture leads, fashion follows."

## Tech Stack

- Python 3
- `bird` CLI for Twitter data
- GitHub Actions for automation
- Multi-source data aggregation
- Real-time trend scoring

## Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/codebyellalesperance/taste-analytics.git
cd taste-analytics
```

### 2. Set up credentials (IMPORTANT 🔒)

**Never commit secrets to git!**

For local development:
```bash
# Copy the template
cp .env.example .env

# Edit .env and add your credentials
# Get Twitter cookies from your browser after logging in
```

For GitHub Actions:
- Go to `Settings → Secrets and variables → Actions`
- Add `TWITTER_AUTH_TOKEN` and `TWITTER_CT0`
- See `AUTOMATION.md` for full setup

### 3. Run scripts

```bash
# Install dependencies
pip install requests

# Run individual collectors
python3 scripts/collect_tiktok.py
python3 scripts/collect_twitter.py
python3 scripts/collect_stockx.py

# Run full analysis
python3 scripts/ultimate_dashboard.py

# Generate posts
python3 scripts/generate_posts.py
```

## Automation

The repo includes GitHub Actions workflows that run automatically:

- **Every 3 hours**: Full scan + auto-post 3 tweets
- **Manual**: Post on-demand from Actions tab

See [`AUTOMATION.md`](AUTOMATION.md) for complete setup guide.

## Security

🔒 **Never commit API keys, tokens, or credentials to git.**

- Credentials go in `.env` (gitignored) or GitHub Secrets
- See [`SECURITY.md`](SECURITY.md) for best practices
- `.env.example` shows the template

## Sample Output

### Trend Scores
```
📈 TREND SCORES (0-100):
opiumcore       [████████░░░░░░░░░░░░]  40/100
archivefashion  [████████░░░░░░░░░░░░]  40/100
chrome hearts   [█░░░░░░░░░░░░░░░░░░░]   6/100
```

### Cross-Platform Insights
```
🧠 CROSS-PLATFORM INSIGHTS:
1. Audio trend alert: 'Femininomenon by Chappell Roan' with 234,000 uses 
   directly driving coquette aesthetic. Music is the new fashion marketing.

2. PREDICTION: #archivefashion will peak in 7-14 days. Currently at 34M views 
   with +567% growth. Early movers should exit soon.

3. DEATH WATCH: #quietluxury down -67% on TikTok. The algorithm has moved on. 
   Brands still pushing this are already late.
```

### Generated Posts
```
1. Trend scores right now: opiumcore (40/100), archivefashion (40/100), 
   gorpcore (9/100). The algorithm has spoken.

2. Extreme Shoulders on 27 runways. Street adoption: 3%. Balenciaga's $4,000 
   jackets about to hit clearance.

3. Platform breakdown for 'opiumcore': TikTok (explosive), StockX (rising), 
   Reddit (positive). Triple confirmation = real trend.
```

## Architecture

```
Data Sources                Analysis                Output
━━━━━━━━━━━━━━            ━━━━━━━━━━━━━━         ━━━━━━━━━━━━━━
TikTok                     Trend Scoring           Twitter Posts
Twitter          →         Correlation    →        Data Commits
Reddit                     Predictions             Artifacts
StockX                     Gap Analysis
Runway
Super Bowl
```

## Project Structure

```
taste-analytics/
├── .github/workflows/     # Automation workflows
├── scripts/               # Data collectors & analyzers
│   ├── collect_tiktok.py
│   ├── collect_twitter.py
│   ├── collect_stockx.py
│   ├── collect_reddit.py
│   ├── collect_runway.py
│   ├── collect_superbowl.py
│   ├── dashboard.py
│   ├── generate_posts.py
│   ├── master_analyzer.py
│   └── ultimate_dashboard.py
├── data/                  # Generated data (gitignored)
├── output/                # Generated posts (gitignored)
├── .env.example           # Credential template
├── AUTOMATION.md          # Automation setup guide
├── SECURITY.md            # Security best practices
└── README.md              # This file
```

## Use Cases

### For Content Creators (@tasteengine)
- Auto-post data-driven trend insights
- Stay ahead of mainstream coverage
- Build authority with real metrics

### For Brands (B2B SaaS potential)
- See what Fashion Week got wrong
- Know which Super Bowl ads will flop
- Predict trend peaks before they happen
- Never waste money on dead trends

**The pitch:**
> "We would have saved BMW $10.5M. We would have told Balenciaga to skip extreme shoulders. We saw mob wife before Vogue. Pay us $5K/month to never waste money again."

## YC Application Potential

**One-liner:**  
"Bloomberg Terminal for consumer culture. We tell brands what's going to be cool before it's cool."

**Why now:**
- AI can finally process culture at scale
- Brands desperate for TikTok-speed insights
- Death of cookies = need new intelligence

**Business model:**
- Free: @tasteengine Twitter content
- $5K/month: Real-time dashboard for brands
- 100 brands = $6M ARR

## Contributing

This is currently a private project. If you have access:

1. Never commit secrets (use `.env` or GitHub Secrets)
2. Follow the security guidelines in `SECURITY.md`
3. Run scripts locally before pushing
4. Test automation workflows before enabling

## Cost

**GitHub Actions:** Free (2,000 min/month, we use ~480)  
**Data sources:** Free (public APIs and scraping)  
**Total:** $0/month ✅

## License

Private - All rights reserved

---

Built by @tasteengine | Follow for real-time trend updates  
Questions? Open an issue or check the docs: [`AUTOMATION.md`](AUTOMATION.md) | [`SECURITY.md`](SECURITY.md)
