# 🚀 DeepDive AI - Shuru Kare (START HERE)

## ✅ Aapke paas sab API keys hai! Bas set karna hai.

---

## 📋 Quick Checklist (5 Minute Setup)

### **Step 1: .env File Banaye**

**Windows Terminal/CMD mein:**
```bash
cd backend
copy .env.example .env
```

Isse `backend` folder mein `.env` naam ki nayi file ban jayegi.

---

### **Step 2: .env File Open Kare**

**Kaise?**
- Right-click on `.env` file
- "Open with" → Notepad
- Ya koi bhi text editor use kare

---

### **Step 3: Apni API Keys Dale**

`.env` file mein ye lines dikhegi:

```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
COINGECKO_API_KEY=your_coingecko_api_key_here
TWITTER_BEARER_TOKEN=your_twitter_bearer_token_here
GITHUB_TOKEN=your_github_token_here
```

**Replace kare:**
- `your_openrouter_api_key_here` → Apni actual OpenRouter key
- `your_coingecko_api_key_here` → Apni actual CoinGecko key
- `your_twitter_bearer_token_here` → Apni actual Twitter token
- `your_github_token_here` → Apni actual GitHub token

**Example (Sample):**
```env
OPENROUTER_API_KEY=sk-or-v1-1a2b3c4d5e6f7g8h9i0j
COINGECKO_API_KEY=CG-AbCdEfGh1234567890
TWITTER_BEARER_TOKEN=AAAAAAAAAAAAAAAAAAAAAA%2FAAAAAAAxxxxxxxxxxx
GITHUB_TOKEN=ghp_1234567890abcdefghijklmnopqrst
```

---

### **Step 4: File Save Kare**

- **Ctrl + S** press kare
- File close kare

---

### **Step 5: Backend Chalu Kare**

**Option 1: Double-click (Aasan)**
- `start-backend.bat` file par double-click kare
- Ek terminal window khulega

**Option 2: Manual (Terminal mein)**
```bash
cd backend
python main.py
```

**Success dikhega:**
```
INFO:     Uvicorn running on http://0.0.0.0:8000
✅ Backend chal raha hai!
```

---

### **Step 6: Frontend Chalu Kare**

**Naya terminal window kholo**, phir:

**Option 1: Double-click**
- `start-frontend.bat` file par double-click kare

**Option 2: Manual**
```bash
cd frontend
npm run dev
```

**Success dikhega:**
```
➜  Local:   http://localhost:3000/
✅ Frontend chal raha hai!
```

---

### **Step 7: Browser Mein Kholo**

1. **Browser kholo** (Chrome, Edge, Firefox)
2. **Address bar mein type kare:** `http://localhost:3000`
3. **Enter press kare**

**Aapko dikhega:**
- Purple gradient background
- Bada search bar
- "DeepDive AI" heading

✅ **Kaam kar raha hai!**

---

## 🎯 Pehla Analysis Try Kare

1. **Search bar mein type kare:** `Ethereum`
2. **"Analyze" button par click kare**
3. **30 seconds wait kare**
4. **Results dekho!**

Aapko milega:
- ✅ AI-generated summary
- ✅ Score (out of 50)
- ✅ Risk level (Green/Yellow/Red)
- ✅ Investment thesis
- ✅ PDF report download option

---

## 🐛 Agar Kuch Problem Ho

### **Problem 1: Backend start nahi ho raha**

**Error:** "python: command not found"
**Solution:** Python install kare: https://www.python.org/downloads/

**Error:** "No module named 'fastapi'"
**Solution:** 
```bash
cd backend
pip install -r requirements.txt
```

---

### **Problem 2: Frontend start nahi ho raha**

**Error:** "npm: command not found"
**Solution:** Node.js install kare: https://nodejs.org/

**Error:** "Cannot find module"
**Solution:**
```bash
cd frontend
npm install
```

---

### **Problem 3: Analysis fail ho raha hai**

**Error:** "OpenRouter API key not configured"
**Solution:** 
- Check kare `.env` file `backend` folder mein hai
- Check kare `OPENROUTER_API_KEY` properly set hai
- Spaces nahi hone chahiye `=` ke around

**Sahi tarika:**
```env
OPENROUTER_API_KEY=sk-or-v1-xxxxx
```

**Galat tarika:**
```env
OPENROUTER_API_KEY = sk-or-v1-xxxxx  ❌ (spaces hai)
```

---

### **Problem 4: "Port 8000 already in use"**

**Solution:**
- Pehle se koi backend chal raha hai
- Close karo ya naya terminal use karo

---

## 📚 Aur Help Chahiye?

### **Detailed Guides (English + Hindi):**
1. **SETUP_YOUR_KEYS.md** - API keys kaise get kare (Step-by-step)
2. **OPENROUTER_CHANGES.md** - Kya changes huye
3. **QUICKSTART.md** - Quick English guide
4. **SETUP_GUIDE.md** - Complete setup (English)

---

## 🔑 API Keys Kaha Se Mile?

### **1. OpenRouter (Zaruri - AI ke liye)**
- Website: https://openrouter.ai/
- Sign up kare
- Keys section mein jao
- New key banao
- **Free credit:** $1 (650+ analyses!)

### **2. CoinGecko (Zaruri - Crypto data ke liye)**
- Website: https://www.coingecko.com/en/api
- "Get Your Free API Key" par click kare
- Sign up kare
- Dashboard se copy kare

### **3. Twitter (Optional - Social metrics ke liye)**
- Website: https://developer.twitter.com
- Project banao
- App banao
- Bearer Token generate kare

### **4. GitHub (Optional - Dev metrics ke liye)**
- Website: https://github.com/settings/tokens
- "Generate new token" par click kare
- Scopes select kare: repo, read:org, read:user
- Token copy kare (turant! dubara nahi dikhega)

---

## ✅ Summary (Sankshep)

**Kya karna hai:**
1. ✅ `.env` file banao (`copy .env.example .env`)
2. ✅ Apni API keys dale
3. ✅ File save karo
4. ✅ Backend start karo (`start-backend.bat` ya `python main.py`)
5. ✅ Frontend start karo (`start-frontend.bat` ya `npm run dev`)
6. ✅ Browser mein `http://localhost:3000` kholo
7. ✅ "Ethereum" search karo
8. ✅ Results dekho! 🎉

**Kitna time lagega:** 5-10 minutes (agar API keys ready hai)

**Kitna cost:** $0 (free credits se start karo!)

---

## 🎓 Kya-Kya Kar Sakte Hai

### **1. Project Analysis**
- Kisi bhi crypto project ka naam dale
- Contract address bhi dal sakte ho
- Twitter handle bhi (@uniswap)
- 30 seconds mein full report!

### **2. Showcase Dekho**
- "Showcase" tab par click karo
- 20+ pre-analyzed projects dekho
- Category se filter karo
- Instant results!

### **3. Projects Compare Karo**
- "Compare" tab par click karo
- 2-3 project names dale
- Side-by-side comparison dekho
- Best option choose karo!

### **4. PDF Report Download**
- Har analysis ke baad
- "Download PDF Report" button
- Professional 2-page report
- Share kar sakte ho!

---

## 💡 Pro Tips

1. **Popular projects se start karo** (Ethereum, Bitcoin)
   - Sabse zyada data hai
   - Results best aate hai

2. **Showcase use karo** quick results ke liye
   - Waiting nahi karni padegi
   - Instant analysis

3. **API keys secure rakho**
   - Kabhi share mat karo
   - Git pe upload mat karo

4. **Free models bhi try karo**
   - OpenRouter pe free models hai
   - Credit bachao!

---

## 🆘 Abhi Bhi Problem?

### **Check kare:**
1. ✅ Python installed hai? (`python --version`)
2. ✅ Node.js installed hai? (`node --version`)
3. ✅ `.env` file `backend` folder mein hai?
4. ✅ API keys sahi hai?
5. ✅ Internet connection chal raha hai?

### **Terminal mein dekho:**
- Backend terminal: Errors dikhenge
- Frontend terminal: Errors dikhenge
- Browser console (F12): Frontend errors

---

## 🎉 Taiyar Hai!

Sab set hai! Ab bas:

```bash
# Terminal 1
start-backend.bat

# Terminal 2  
start-frontend.bat

# Browser
http://localhost:3000
```

**Search karo "Ethereum" aur dekho magic! ✨**

---

## 📞 Contact

**Agar stuck ho:**
1. Error message dhyan se padho
2. Documentation files check karo
3. Google par search karo error message

**Files:**
- `SETUP_YOUR_KEYS.md` - Detailed API key guide
- `OPENROUTER_CHANGES.md` - What changed
- `QUICKSTART.md` - English quick guide

---

**Shubh Kamnaye! Good luck! 🚀📊💎**

*Crypto research ab 60 seconds mein!*
