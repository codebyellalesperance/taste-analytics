# Automation Setup Guide

This repo includes automated workflows that scan trends and post to Twitter.

## 🤖 What Gets Automated

**Every 3 hours, the system:**
1. Scans TikTok, Twitter, Reddit, StockX, Runway, and Super Bowl ads
2. Analyzes cross-platform correlations
3. Generates data-driven posts
4. Auto-posts 3 tweets to @tasteengine
5. Commits updated data back to the repo

## 📋 Setup Instructions

### 1. Add GitHub Secrets

Go to your repo settings: `Settings → Secrets and variables → Actions`

Add these secrets:

**TWITTER_AUTH_TOKEN**
```
<your-twitter-auth-token>
```

**TWITTER_CT0**
```
<your-twitter-ct0-token>
```

(Get these from your browser cookies after logging into Twitter)

### 2. Enable GitHub Actions Permissions

1. Go to `Settings → Actions → General`
2. Under "Workflow permissions" select **"Read and write permissions"**
3. Check **"Allow GitHub Actions to create and approve pull requests"**
4. Save

### 3. Enable Workflows

1. Go to `Actions` tab in your repo
2. Enable GitHub Actions if prompted
3. You'll see two workflows:
   - **Automated Trend Scanning & Posting** (runs every 3 hours)
   - **Manual Post to Twitter** (run on demand)

### 4. Test It

**Manual test:**
1. Go to `Actions` tab
2. Select "Automated Trend Scanning & Posting"
3. Click "Run workflow" → "Run workflow"
4. Watch it run (takes ~2 minutes)

**Check the output:**
- Check Twitter (@tasteengine) for new posts
- Check `Actions` tab for logs
- Check repo for new data commits

## ⏰ Schedule

The automation runs:
- **Every 3 hours:** Full scan + 3 posts
- **Times:** 12am, 3am, 6am, 9am, 12pm, 3pm, 6pm, 9pm UTC

To change the schedule, edit `.github/workflows/auto-trend-scan.yml`:
```yaml
schedule:
  - cron: '0 */3 * * *'  # Every 3 hours
  # Or:
  - cron: '0 9,15,21 * * *'  # 9am, 3pm, 9pm only
```

## 🔒 Security

**Secrets are encrypted by GitHub.** They:
- Never appear in logs
- Can't be read by forks
- Are only accessible to workflow runs

**To rotate credentials:**
1. Generate new Twitter cookies
2. Update secrets in repo settings
3. No code changes needed

## 📊 What Gets Stored

Each run saves:
- `data/*_latest.json` - Latest scan results
- `output/posts.txt` - Generated tweets
- `output/ultimate_analysis.json` - Full analysis

Data is auto-committed back to the repo for history.

## 🚨 Troubleshooting

**"Twitter API error 226"**
- Account might be flagged for automation
- Wait 24-48 hours, manually post a few tweets
- Try again

**"No posts generated"**
- Check data files exist in `data/` folder
- Run scripts locally first to debug

**"Permission denied on push"**
- GitHub Actions needs write permissions
- Go to `Settings → Actions → General`
- Under "Workflow permissions" select "Read and write"

## 🎯 Customization

**Change posting frequency:**
Edit the `cron` schedule in `auto-trend-scan.yml`

**Change number of posts:**
Edit the "Post to Twitter" step - add/remove `bird tweet` calls

**Change data sources:**
Comment out steps you don't want:
```yaml
# - name: Scan Reddit sentiment
#   run: python3 scripts/collect_reddit.py
```

**Add new data sources:**
Add a new step:
```yaml
- name: Scan Instagram trends
  run: python3 scripts/collect_instagram.py
```

## 💰 Cost

**GitHub Actions free tier:**
- 2,000 minutes/month
- Each run takes ~2 minutes
- 8 runs/day × 30 days = 480 minutes/month
- **Completely free** ✅

## 📈 Scaling

When you hit limits:
1. Reduce frequency (every 6 hours instead of 3)
2. Split into separate workflows
3. Use GitHub Actions paid plan ($4/month for 3,000 minutes)
4. Move to your own server

---

Built with ❤️ by Taste Engine
