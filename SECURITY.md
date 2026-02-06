# Security Best Practices

## ⚠️ Never Commit Secrets

**Never commit these to git:**
- API keys
- Authentication tokens
- Passwords
- Cookie values
- Private keys

## ✅ How to Handle Secrets

### For GitHub Actions
Store secrets in: `Settings → Secrets and variables → Actions`

### For Local Development
1. Copy `.env.example` to `.env`
2. Add your actual credentials to `.env`
3. `.env` is gitignored and will never be committed

### For Python Scripts
```python
import os
from dotenv import load_dotenv

load_dotenv()

TWITTER_AUTH = os.getenv('TWITTER_AUTH_TOKEN')
TWITTER_CT0 = os.getenv('TWITTER_CT0')
```

## 🔍 How to Check for Leaked Secrets

Before committing:
```bash
# Check what you're about to commit
git diff --cached

# Search for potential secrets
git diff --cached | grep -i "token\|key\|password\|secret"
```

## 🚨 If You Accidentally Commit Secrets

1. **Revoke the credentials immediately**
   - Twitter: Log out all sessions, get new cookies
   - GitHub tokens: Delete the token at https://github.com/settings/tokens

2. **Remove from git history**
   ```bash
   git filter-branch --force --index-filter \
     "git rm --cached --ignore-unmatch <file-with-secret>" \
     --prune-empty --tag-name-filter cat -- --all
   
   git push --force
   ```

3. **Generate new credentials**

## 📝 What's Safe to Commit

✅ Configuration templates (`.env.example`)  
✅ Public configuration  
✅ Code that *uses* environment variables  
✅ Documentation  

❌ Actual credential values  
❌ `.env` files  
❌ Cookie dumps  
❌ API responses with tokens  

## 🔐 Current Setup

**Local development:**
- Credentials in `.env` (gitignored)
- Scripts read from environment variables

**GitHub Actions:**
- Credentials in repository secrets
- Workflows reference `${{ secrets.SECRET_NAME }}`
- Never logged or exposed

## 🛡️ Additional Security

**Rotate credentials regularly:**
- Twitter cookies: Every 30 days
- GitHub tokens: Every 90 days or when team members leave

**Limit token scope:**
- Only grant permissions actually needed
- GitHub: `repo` + `workflow` (not `admin`)
- Twitter: Read/write (not admin)

**Monitor for leaks:**
- GitHub has secret scanning enabled by default
- Check email for alerts
- Use tools like `git-secrets` or `gitleaks`

---

**Remember:** If it's secret, it shouldn't be in git. Ever.
