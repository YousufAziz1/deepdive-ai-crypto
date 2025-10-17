# DeepDive AI - Quick Start Guide

Get up and running in 5 minutes!

## ⚡ Prerequisites

Install these first:
- Python 3.9+ → [Download](https://www.python.org/downloads/)
- Node.js 18+ → [Download](https://nodejs.org/)

## 🚀 Quick Setup

### Step 1: Get API Keys (5 minutes)

You need at least the **CoinGecko API key** to start:

1. **CoinGecko** (Required): https://www.coingecko.com/en/api
2. **Sentient ROMA** (For AI features): https://sentient.xyz
3. **Twitter** (Optional): https://developer.twitter.com
4. **GitHub** (Optional): https://github.com/settings/tokens

### Step 2: Configure Environment

1. Navigate to `backend` folder
2. Copy `.env.example` to `.env`
3. Open `.env` and add your API keys:

```env
ROMA_API_KEY=your_roma_key_here
COINGECKO_API_KEY=your_coingecko_key_here
TWITTER_BEARER_TOKEN=your_twitter_token_here
GITHUB_TOKEN=your_github_token_here
```

### Step 3: Start the Application

#### Option A: Using Scripts (Windows)

Double-click these files:
1. `start-backend.bat` (starts API server)
2. `start-frontend.bat` (starts web interface)

#### Option B: Manual Start

**Terminal 1 - Backend:**
```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux
pip install -r requirements.txt
python main.py
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm install
npm run dev
```

### Step 4: Open Application

Visit: **http://localhost:3000**

You should see the DeepDive AI homepage!

## 🎯 Your First Analysis

1. In the search bar, type: **Ethereum**
2. Click **Analyze**
3. Wait 10-30 seconds
4. Review the comprehensive report!

## ✅ Success Indicators

You'll know it's working when you see:

**Backend (Terminal 1):**
```
INFO:     Uvicorn running on http://0.0.0.0:8000
```

**Frontend (Terminal 2):**
```
➜  Local:   http://localhost:3000/
```

**Browser:**
- Purple gradient homepage
- Search bar with "Analyze" button
- Navigation menu (Analyze, Showcase, Compare)

## 🐛 Troubleshooting

### "Backend not starting"
- Check Python version: `python --version` (need 3.9+)
- Install dependencies: `pip install -r requirements.txt`
- Check `.env` file exists in backend folder

### "Frontend not starting"
- Check Node version: `node --version` (need 18+)
- Delete `node_modules` and run `npm install` again
- Try port 5173 if 3000 is taken

### "Analysis fails"
- Verify `.env` has API keys
- Check backend is running (visit http://localhost:8000)
- Try "Ethereum" first (most reliable)
- Check API key validity

### "Can't connect to backend"
- Ensure backend is running on port 8000
- Check firewall isn't blocking
- Verify CORS settings in `.env`

## 🎓 Next Steps

1. **Try Different Projects**
   - Chainlink
   - Uniswap
   - Bitcoin

2. **Use Showcase**
   - Click "Showcase" to see 20+ pre-analyzed projects

3. **Compare Projects**
   - Click "Compare"
   - Enter 2-3 project names
   - Get side-by-side analysis

4. **Generate Reports**
   - After analysis, click "Download PDF Report"

5. **Explore API**
   - Visit http://localhost:8000/docs
   - Test endpoints interactively

## 📚 Learn More

- **Full Setup Guide**: See `SETUP_GUIDE.md`
- **API Documentation**: See `API_DOCUMENTATION.md`
- **Demo Guide**: See `DEMO_GUIDE.md`

## 💡 Pro Tips

1. **Start with popular projects** (Ethereum, Bitcoin) - they have the most complete data
2. **Use Showcase** for instant results without waiting
3. **Compare similar projects** for better insights
4. **Check `/docs` endpoint** for API testing

## 🆘 Getting Help

Having issues?

1. Read error messages carefully
2. Check SETUP_GUIDE.md for detailed troubleshooting
3. Verify all API keys are valid
4. Ensure both backend AND frontend are running

## 🎉 You're Ready!

Start analyzing crypto projects and making data-driven decisions!

---

**Time to First Analysis**: ~5 minutes  
**Learning Curve**: Beginner-friendly  
**Support**: See README.md for contact info
