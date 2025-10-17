# 🔑 API Keys Setup Guide - OpenRouter Version

## Step-by-Step Instructions (Hindi + English)

---

## ✅ Step 1: Create .env File

**English:**
1. Go to `backend` folder
2. Copy `.env.example` file
3. Rename the copy to `.env`

**Hindi:**
1. `backend` folder mein jaye
2. `.env.example` file ko copy kare
3. Copy ko rename karke `.env` bana de

**Command (Terminal/CMD):**
```bash
cd backend
copy .env.example .env
```

---

## ✅ Step 2: Add Your API Keys

Open the `.env` file in Notepad or any text editor and fill in your keys:

```env
# API Keys
OPENROUTER_API_KEY=sk-or-v1-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
COINGECKO_API_KEY=CG-xxxxxxxxxxxxxxxxxxxxxxxx
TWITTER_BEARER_TOKEN=AAAAAAAAAAAAAAAAAAAAAxxxxxxxxx
GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxxxxxx
DEFILLAMA_API_KEY=optional

# Server Configuration (Don't change these)
HOST=0.0.0.0
PORT=8000
DEBUG=True

# CORS Settings (Don't change these)
CORS_ORIGINS=http://localhost:3000,http://localhost:5173
```

---

## 🔑 Where to Put Each API Key

### 1️⃣ **OpenRouter API Key**

**English:**
- Website: https://openrouter.ai/
- Sign up for account
- Go to Keys section
- Create new API key
- Copy and paste in `.env` file

**Hindi:**
- Website: https://openrouter.ai/
- Account banaye
- Keys section mein jaye
- Naya API key banaye
- Copy karke `.env` file mein paste kare

**Example:**
```env
OPENROUTER_API_KEY=sk-or-v1-1234567890abcdefghijklmnopqrstuvwxyz
```

**Free Credits:** OpenRouter gives $1 free credit to start!

---

### 2️⃣ **CoinGecko API Key**

**English:**
- Website: https://www.coingecko.com/en/api
- Click "Get Your Free API Key"
- Sign up
- Copy API key from dashboard

**Hindi:**
- Website: https://www.coingecko.com/en/api
- "Get Your Free API Key" par click kare
- Sign up kare
- Dashboard se API key copy kare

**Example:**
```env
COINGECKO_API_KEY=CG-AbCdEfGhIjKlMnOpQrStUv
```

**Free Tier:** 30 API calls per minute (enough for testing)

---

### 3️⃣ **Twitter Bearer Token** (Optional but Recommended)

**English:**
- Website: https://developer.twitter.com/en/portal/dashboard
- Create new project
- Create new app
- Go to "Keys and tokens"
- Generate Bearer Token
- Copy it

**Hindi:**
- Website: https://developer.twitter.com/en/portal/dashboard
- Naya project banaye
- Naya app banaye
- "Keys and tokens" mein jaye
- Bearer Token generate kare
- Copy kare

**Example:**
```env
TWITTER_BEARER_TOKEN=AAAAAAAAAAAAAAAAAAAA%2FAAAAAAAxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

**Note:** Without Twitter token, social metrics won't work (but app will still run)

---

### 4️⃣ **GitHub Token** (Optional but Recommended)

**English:**
- Website: https://github.com/settings/tokens
- Click "Generate new token (classic)"
- Select scopes: `repo`, `read:org`, `read:user`
- Click "Generate token"
- **IMPORTANT:** Copy immediately (you can't see it again!)

**Hindi:**
- Website: https://github.com/settings/tokens
- "Generate new token (classic)" par click kare
- Scopes select kare: `repo`, `read:org`, `read:user`
- "Generate token" par click kare
- **IMPORTANT:** Turant copy kar le (dubara nahi dikhega!)

**Example:**
```env
GITHUB_TOKEN=ghp_1234567890abcdefghijklmnopqrstuvwxyz12
```

**Note:** Without GitHub token, you get only 60 API calls/hour (with token: 5000/hour)

---

### 5️⃣ **DefiLlama API Key** (Optional - Skip for now)

This is optional and rarely needed. You can leave it as:
```env
DEFILLAMA_API_KEY=optional
```

---

## ✅ Complete Example .env File

Copy this and fill in YOUR keys:

```env
# ========================================
# DeepDive AI - API Keys Configuration
# ========================================

# AI Analysis (OpenRouter instead of Sentient ROMA)
OPENROUTER_API_KEY=sk-or-v1-YOUR_OPENROUTER_KEY_HERE

# Crypto Data (CoinGecko)
COINGECKO_API_KEY=CG-YOUR_COINGECKO_KEY_HERE

# Social Metrics (Twitter) - Optional but recommended
TWITTER_BEARER_TOKEN=YOUR_TWITTER_BEARER_TOKEN_HERE

# Development Metrics (GitHub) - Optional but recommended
GITHUB_TOKEN=ghp_YOUR_GITHUB_TOKEN_HERE

# DeFi Data (DefiLlama) - Optional
DEFILLAMA_API_KEY=optional

# ========================================
# Server Configuration (DON'T CHANGE)
# ========================================
HOST=0.0.0.0
PORT=8000
DEBUG=True

# CORS Settings (DON'T CHANGE)
CORS_ORIGINS=http://localhost:3000,http://localhost:5173
```

---

## 🚨 Important Notes (Zaruri Baatein)

### **English:**
1. **Never share your API keys** - They're like passwords
2. **Never commit .env to git** - It's already in .gitignore
3. **Replace ALL the placeholder text** with your actual keys
4. **Minimum requirement:** You MUST have at least OpenRouter and CoinGecko keys
5. **Optional keys:** Twitter and GitHub are optional but give better results
6. **Save the file** after adding keys

### **Hindi:**
1. **API keys kabhi share mat kare** - Ye password jaise hai
2. **`.env` file git pe upload mat kare** - .gitignore mein already hai
3. **Placeholder text replace kare** apni actual keys se
4. **Minimum requirement:** Kam se kam OpenRouter aur CoinGecko keys chahiye
5. **Optional keys:** Twitter aur GitHub optional hai par better results dete hai
6. **File save karna mat bhule** keys add karne ke baad

---

## ✅ Verification (Check Kare)

After setting up, your `.env` file should look like:

```
OPENROUTER_API_KEY=sk-or-v1-[long string]
COINGECKO_API_KEY=CG-[alphanumeric string]
TWITTER_BEARER_TOKEN=AAAA[very long string]  # Optional
GITHUB_TOKEN=ghp_[alphanumeric string]        # Optional
```

**NOT like this (wrong):**
```
OPENROUTER_API_KEY=your_openrouter_api_key_here  ❌ WRONG
COINGECKO_API_KEY=YOUR_COINGECKO_KEY_HERE      ❌ WRONG
```

---

## 🚀 Testing (Test Kare)

After adding keys:

1. **Start backend:**
   ```bash
   cd backend
   python main.py
   ```

2. **Check for errors:**
   - If you see "OpenRouter API key not configured" → Check OPENROUTER_API_KEY
   - If you see "Uvicorn running on..." → ✅ Success!

3. **Test API:**
   Visit: http://localhost:8000/docs
   
---

## 💰 API Costs (Kharcha)

| Service | Free Tier | Cost |
|---------|-----------|------|
| **OpenRouter** | $1 free credit | ~$0.0015 per analysis |
| **CoinGecko** | 30 calls/min | Free forever |
| **Twitter** | 500k tweets/month | Free (v2 API) |
| **GitHub** | 5000 calls/hour | Free |

**Total cost for 100 analyses:** ~$0.15 (very cheap!)

---

## 🆘 Help (Madad)

### Common Errors:

**Error: "OpenRouter API key not configured"**
- Solution: Check if OPENROUTER_API_KEY is set in .env file
- Hindi: `.env` file mein OPENROUTER_API_KEY check kare

**Error: "Module not found"**
- Solution: Run `pip install -r requirements.txt`
- Hindi: `pip install -r requirements.txt` chalaye

**Error: "Port 8000 already in use"**
- Solution: Close other programs using port 8000
- Hindi: Port 8000 use karne wale dusre program band kare

---

## 📞 Quick Reference

**Minimum Required Keys:**
1. ✅ OpenRouter (for AI analysis)
2. ✅ CoinGecko (for crypto data)

**Optional but Recommended:**
3. ⭐ Twitter (for social metrics)
4. ⭐ GitHub (for dev metrics)

**Can Skip:**
5. ❌ DefiLlama (rarely used)

---

## ✅ You're Done! (Ho Gaya!)

Once all keys are added:
1. Save .env file
2. Run `start-backend.bat`
3. Run `start-frontend.bat`
4. Open http://localhost:3000
5. Search "Ethereum"
6. Enjoy! 🎉

---

**Need more help?** See `QUICKSTART.md` or `SETUP_GUIDE.md`
