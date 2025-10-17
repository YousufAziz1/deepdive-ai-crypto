# DeepDive AI - Complete Setup Guide

This guide will walk you through setting up DeepDive AI from scratch on your local machine.

## 📋 Prerequisites Checklist

Before you begin, ensure you have:

- [ ] Python 3.9 or higher installed
- [ ] Node.js 18 or higher installed
- [ ] Git installed
- [ ] Text editor (VS Code recommended)
- [ ] Terminal/Command Prompt access

## 🔑 Step 1: Obtain API Keys

### 1.1 Sentient ROMA API Key

1. Visit [https://sentient.xyz](https://sentient.xyz)
2. Sign up for an account
3. Navigate to API section
4. Generate a new API key
5. Save it securely

### 1.2 CoinGecko API Key

1. Go to [https://www.coingecko.com/en/api](https://www.coingecko.com/en/api)
2. Click "Get Your Free API Key"
3. Sign up and verify email
4. Copy your API key from the dashboard

### 1.3 Twitter API Bearer Token

1. Visit [https://developer.twitter.com/en/portal/dashboard](https://developer.twitter.com/en/portal/dashboard)
2. Create a new project and app
3. Generate Bearer Token
4. Save the token

### 1.4 GitHub Personal Access Token

1. Go to [https://github.com/settings/tokens](https://github.com/settings/tokens)
2. Click "Generate new token (classic)"
3. Select scopes: `repo`, `read:org`, `read:user`
4. Generate and save token

## ⚙️ Step 2: Backend Setup

### 2.1 Navigate to Backend Directory

```bash
cd backend
```

### 2.2 Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt.

### 2.3 Install Python Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

This will install:
- FastAPI (web framework)
- uvicorn (ASGI server)
- httpx, aiohttp (async HTTP clients)
- pycoingecko (CoinGecko wrapper)
- PyGithub (GitHub API wrapper)
- tweepy (Twitter API wrapper)
- reportlab (PDF generation)
- and more...

### 2.4 Configure Environment Variables

1. Copy the example environment file:
```bash
copy .env.example .env
```

2. Open `.env` in your text editor

3. Fill in your API keys:
```env
ROMA_API_KEY=sk_your_roma_api_key_here
COINGECKO_API_KEY=CG-your_coingecko_key_here
TWITTER_BEARER_TOKEN=your_twitter_bearer_token_here
GITHUB_TOKEN=ghp_your_github_token_here

HOST=0.0.0.0
PORT=8000
DEBUG=True

CORS_ORIGINS=http://localhost:3000,http://localhost:5173
```

4. Save the file

### 2.5 Test Backend

Start the backend server:
```bash
python main.py
```

You should see:
```
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000
```

Visit `http://localhost:8000` in your browser - you should see:
```json
{
  "status": "healthy",
  "service": "DeepDive AI - Crypto Research Agent",
  "version": "1.0.0"
}
```

Visit `http://localhost:8000/docs` to see interactive API documentation.

**Keep this terminal open** - the backend needs to run continuously.

## 🎨 Step 3: Frontend Setup

Open a **new terminal window**.

### 3.1 Navigate to Frontend Directory

```bash
cd frontend
```

### 3.2 Install Node Dependencies

```bash
npm install
```

This will install:
- React 18
- Vite (build tool)
- TailwindCSS (styling)
- Lucide React (icons)
- Axios (HTTP client)
- React Router (navigation)

Wait for installation to complete (may take 1-2 minutes).

### 3.3 Start Development Server

```bash
npm run dev
```

You should see:
```
  VITE v5.0.8  ready in 500 ms

  ➜  Local:   http://localhost:3000/
  ➜  Network: use --host to expose
  ➜  press h to show help
```

### 3.4 Open Application

1. Open your browser
2. Go to `http://localhost:3000`
3. You should see the DeepDive AI homepage with:
   - Purple gradient background
   - Search bar in the center
   - "How It Works" section

## ✅ Step 4: Verify Installation

### 4.1 Test Basic Search

1. In the search bar, type: `Ethereum`
2. Click "Analyze"
3. Wait 10-30 seconds
4. You should see analysis results with:
   - Executive summary
   - Scores (0-50)
   - Risk assessment
   - Investment thesis

### 4.2 Test API Directly

Open a new terminal and test the API:

```bash
curl -X POST "http://localhost:8000/api/v1/analyze" \
  -H "Content-Type: application/json" \
  -d "{\"input\": \"Bitcoin\"}"
```

You should get a JSON response with project data.

### 4.3 Check Showcase

1. Click "Showcase" in the navigation
2. You should see 20+ pre-loaded projects
3. Click "Analyze Now" on any project
4. Verify it loads the analysis

## 🐛 Troubleshooting

### Backend Issues

**Error: "No module named 'fastapi'"**
- Solution: Ensure virtual environment is activated and run `pip install -r requirements.txt`

**Error: "Port 8000 already in use"**
- Solution: Change PORT in .env or kill process using port 8000

**Error: "ROMA API key not configured"**
- Solution: Check .env file has correct ROMA_API_KEY

**Error: "Twitter API rate limit"**
- Solution: Normal during development; data fetching will continue without Twitter data

### Frontend Issues

**Error: "npm: command not found"**
- Solution: Install Node.js from https://nodejs.org

**Error: "Module not found"**
- Solution: Delete `node_modules` folder and run `npm install` again

**Error: "Network Error" when analyzing**
- Solution: Verify backend is running on port 8000

**Blank page on localhost:3000**
- Solution: Check browser console (F12) for errors

### API Key Issues

**CoinGecko API failing:**
- Free tier has rate limits (30 calls/minute)
- Consider upgrading to Pro tier for production

**Twitter API authentication errors:**
- Ensure Bearer Token (not API Key) is used
- Check app permissions in Twitter Developer Portal

**GitHub API rate limiting:**
- Authenticated requests: 5000/hour
- Without token: 60/hour

## 🚀 Next Steps

### 1. Customize Configuration

Edit `backend/config.py` to adjust:
- Cache duration
- Rate limiting
- Default values

### 2. Add More Showcase Projects

Use the API to add projects to showcase:

```bash
curl -X POST "http://localhost:8000/api/v1/showcase" \
  -H "Content-Type: application/json" \
  -d @showcase_project.json
```

### 3. Test Project Comparison

1. Navigate to "Compare" tab
2. Enter 2-3 project names
3. Click "Compare Projects"
4. Review side-by-side analysis

### 4. Generate PDF Reports

After analyzing a project, click "Download PDF Report" to get a shareable document.

### 5. Explore API Documentation

Visit `http://localhost:8000/docs` to:
- Test all endpoints
- View request/response schemas
- Understand API capabilities

## 📊 Performance Tips

### For Development:
- Keep both terminals open
- Use `npm run dev` for hot reload
- Enable DEBUG=True in backend .env

### For Production:
- Build frontend: `npm run build`
- Use production ASGI server: `uvicorn main:app --workers 4`
- Set DEBUG=False
- Add caching layer (Redis)
- Use CDN for static files

## 🔒 Security Best Practices

1. **Never commit .env file** - it contains sensitive API keys
2. **Use environment variables** in production deployment
3. **Rotate API keys** regularly
4. **Set up rate limiting** for public deployments
5. **Use HTTPS** in production

## 📚 Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)
- [TailwindCSS Documentation](https://tailwindcss.com/)
- [Sentient ROMA Docs](https://docs.sentient.xyz/)
- [CoinGecko API Docs](https://www.coingecko.com/en/api/documentation)

## 💬 Getting Help

If you encounter issues:

1. Check this setup guide again
2. Review error messages carefully
3. Search GitHub Issues
4. Ask in Discord community
5. Open a new GitHub Issue with:
   - Error message
   - Steps to reproduce
   - Your environment (OS, Python/Node versions)

## ✅ Setup Complete!

You now have a fully functional DeepDive AI installation. Start analyzing crypto projects and generating AI-powered research reports!

Happy researching! 🚀📊
