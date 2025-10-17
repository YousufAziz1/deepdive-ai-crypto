# 🚀 DeepDive AI - Crypto Research Agent

**AI-Powered Crypto Research Platform** with OpenRouter AI Integration

Analyze any crypto project in under 60 seconds with comprehensive AI-driven insights, scoring, and professional PDF reports.

> **Note:** This project is ready for production use. All sensitive data and API keys are protected.

![DeepDive AI](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)
![License](https://img.shields.io/badge/License-MIT-blue)

## 🌟 Features

### Core Capabilities
- **🔍 Multi-Input Analysis**: Search by project name, contract address, or Twitter handle
- **🤖 AI-Powered Insights**: OpenRouter AI (GPT-3.5-turbo) generates executive summaries and investment theses
- **📊 Comprehensive Scoring**: 5-category analysis (Team, Product-Market Fit, Tokenomics, Community, Technical)
- **⚠️ Risk Assessment**: Green/Yellow/Red risk flags with detailed analysis
- **📄 PDF Reports**: Beautiful, shareable PDF reports with charts
- **⚖️ Project Comparison**: Side-by-side comparison of up to 3 projects
- **⭐ Showcase Library**: 20+ pre-analyzed top crypto projects
- **📈 Real-Time Data**: Integration with CoinGecko, DefiLlama, GitHub, and Twitter

### Data Sources
- **Token Metrics**: CoinGecko API (price, market cap, volume, FDV)
- **DeFi Metrics**: DefiLlama (TVL, protocol data)
- **Development**: GitHub (commits, contributors, activity)
- **Social**: Twitter (followers, engagement, sentiment)

## 🏗️ Tech Stack

### Backend
- **Framework**: Python 3.9+ with FastAPI
- **AI**: OpenRouter AI (supports GPT-3.5-turbo, GPT-4, Claude, free models)
- **Data APIs**: CoinGecko, DefiLlama, Twitter API v2, GitHub API
- **PDF Generation**: ReportLab with matplotlib for charts
- **Async HTTP**: httpx, aiohttp
- **Security**: Environment variables, .gitignore protection

### Frontend
- **Framework**: React 18 + Vite
- **Styling**: TailwindCSS
- **Icons**: Lucide React
- **Charts**: Recharts
- **Routing**: React Router

## 📦 Installation

### Prerequisites
- Python 3.9+
- Node.js 18+
- API Keys (see Configuration section)

### Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
copy .env.example .env
# Edit .env with your API keys
```

### Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

## ⚙️ Configuration

Create a `.env` file in the `backend` directory with the following:

```env
# API Keys (Required)
OPENROUTER_API_KEY=your_openrouter_api_key_here
COINGECKO_API_KEY=your_coingecko_api_key_here

# Optional but Recommended
TWITTER_BEARER_TOKEN=your_twitter_bearer_token_here
GITHUB_TOKEN=your_github_token_here
DEFILLAMA_API_KEY=optional

# Server Config
HOST=0.0.0.0
PORT=8000
DEBUG=True

# CORS
CORS_ORIGINS=http://localhost:3000,http://localhost:5173
```

### Getting API Keys

1. **OpenRouter API** (Required): 
   - Visit: [https://openrouter.ai/](https://openrouter.ai/)
   - Sign up for free account
   - Get $1 free credit (~650 analyses with GPT-3.5-turbo!)
   - Navigate to Keys section
   - Create API key (starts with `sk-or-v1-...`)

2. **CoinGecko** (Required):
   - Visit: [https://www.coingecko.com/en/api](https://www.coingecko.com/en/api)
   - Click "Get Your Free API Key"
   - Sign up and copy API key from dashboard
   - Free tier: 30 calls/minute (sufficient for testing)

3. **Twitter API v2** (Optional but recommended):
   - Visit: [https://developer.twitter.com](https://developer.twitter.com)
   - Create new project and app
   - Generate Bearer Token
   - Provides social metrics and sentiment

4. **GitHub Personal Access Token** (Optional but recommended):
   - Visit: [https://github.com/settings/tokens](https://github.com/settings/tokens)
   - Generate new token (classic)
   - Select scopes: `repo`, `read:org`, `read:user`
   - Copy immediately (won't be shown again!)
   - Increases rate limit: 60 → 5000 requests/hour

## 🚀 Usage

### Starting the Application

**Terminal 1 - Backend:**
```bash
cd backend
python main.py
```
Backend runs on: `http://localhost:8000`

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```
Frontend runs on: `http://localhost:3000`

### API Documentation

Visit `http://localhost:8000/docs` for interactive Swagger API documentation.

### Example API Calls

**Analyze a project:**
```bash
curl -X POST "http://localhost:8000/api/v1/analyze" \
  -H "Content-Type: application/json" \
  -d '{"input": "Ethereum"}'
```

**Compare projects:**
```bash
curl -X POST "http://localhost:8000/api/v1/compare" \
  -H "Content-Type: application/json" \
  -d '{"projects": ["Ethereum", "Render", "Chainlink"]}'
```

**Get quick score:**
```bash
curl "http://localhost:8000/api/v1/quick-score/Ethereum"
```

## 📊 Analysis Output

### Scoring System (0-50)
- **Team Credibility** (0-10): Team background, past projects
- **Product-Market Fit** (0-10): Use case, adoption, demand
- **Tokenomics Health** (0-10): Supply, distribution, vesting
- **Community Strength** (0-10): Social metrics, engagement
- **Technical Development** (0-10): GitHub activity, code quality

### Risk Levels
- **🟢 Green**: Low risk, strong fundamentals
- **🟡 Yellow**: Moderate risk, some concerns
- **🔴 Red**: High risk, significant red flags

### Report Contents
1. Executive Summary (100 words)
2. Key Metrics Dashboard
3. 5-Category Scores
4. Risk Assessment
5. Investment Thesis (Bull/Bear Case)
6. Recommendation

## 🎯 Use Cases

### 1. Quick Due Diligence
Analyze any project in under 60 seconds before investing.

### 2. Portfolio Research
Compare multiple projects to find the best opportunities.

### 3. Daily Monitoring
Track watchlist projects with automated reports.

### 4. Investment Thesis
Generate professional research reports for clients or teams.

## 📁 Project Structure

```
deepdive-ai/
├── backend/
│   ├── main.py                 # FastAPI application
│   ├── config.py               # Configuration
│   ├── requirements.txt        # Python dependencies
│   ├── models/
│   │   └── schemas.py          # Pydantic models
│   ├── routers/
│   │   ├── analysis.py         # Analysis endpoints
│   │   ├── projects.py         # Project management
│   │   └── reports.py          # Report endpoints
│   └── services/
│       ├── aggregation_service.py   # Main orchestrator
│       ├── coingecko_service.py     # CoinGecko API
│       ├── defillama_service.py     # DefiLlama API
│       ├── github_service.py        # GitHub API
│       ├── twitter_service.py       # Twitter API
│       ├── roma_service.py          # Sentient ROMA AI
│       └── report_service.py        # PDF generation
├── frontend/
│   ├── src/
│   │   ├── App.jsx              # Main application
│   │   ├── components/
│   │   │   ├── Header.jsx
│   │   │   ├── SearchBar.jsx
│   │   │   ├── AnalysisResults.jsx
│   │   │   ├── Showcase.jsx
│   │   │   └── Comparison.jsx
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
└── README.md
```

## 🔧 Development

### Running Tests
```bash
cd backend
pytest tests/
```

### Building for Production

**Backend:**
```bash
cd backend
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

**Frontend:**
```bash
cd frontend
npm run build
npm run preview
```

## 🎨 Customization

### Adding New Data Sources
1. Create a new service in `backend/services/`
2. Implement data fetching methods
3. Integrate in `aggregation_service.py`

### Modifying Scoring Algorithm
Edit `backend/services/roma_service.py` to adjust how AI calculates scores.

### Changing AI Model
In `roma_service.py` line ~150, change the model:
```python
# Current (default)
"model": "openai/gpt-3.5-turbo"  # Fast and cheap

# Better quality
"model": "openai/gpt-4-turbo"  # More accurate
"model": "anthropic/claude-3-haiku"  # Good balance

# Free models
"model": "google/gemma-7b-it:free"  # Completely free!
```

### Custom PDF Reports
Modify `report_service.py` to change report layout and content.

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **OpenRouter** for AI API access and free credits
- **CoinGecko** for comprehensive crypto market data
- **DefiLlama** for DeFi protocol data and TVL metrics
- **GitHub** for development activity metrics
- **Twitter** for social analytics and sentiment
- **FastAPI** for excellent Python web framework
- **React & Vite** for modern frontend development

## 📞 Support

- **Documentation**: Check the markdown files in the root directory
  - `QUICKSTART.md` - 5-minute setup guide
  - `SETUP_GUIDE.md` - Detailed installation
  - `API_DOCUMENTATION.md` - Complete API reference
  - `SETUP_YOUR_KEYS.md` - How to get API keys (English + Hindi)
  - `START_HERE_HINDI.md` - Complete Hindi guide
- **Issues**: Create a GitHub issue for bugs or questions
- **API Docs**: Visit `http://localhost:8000/docs` when running

## 🗺️ Roadmap

- [ ] Multi-chain support (Solana, BSC, etc.)
- [ ] Advanced sentiment analysis
- [ ] Price prediction models
- [ ] Telegram/Discord bot integration
- [ ] Mobile app (React Native)
- [ ] Real-time alerts system
- [ ] Portfolio tracking
- [ ] Notion export integration

---

## ⚠️ Important Security Notes

### Before Pushing to GitHub:

1. ✅ **Never commit `.env` file** - It's already in `.gitignore`
2. ✅ **`.env.example` has placeholder values** - No real keys
3. ✅ **`reports/` folder is gitignored** - PDF reports won't be uploaded
4. ✅ **`node_modules/` and `venv/` are excluded** - Clean repo

### Files That Are Safe to Commit:
- ✅ All source code files
- ✅ Configuration files (.gitignore, package.json, requirements.txt)
- ✅ Documentation files (all .md files)
- ✅ `.env.example` (placeholders only)

### Files That Should NEVER Be Committed:
- ❌ `.env` (contains your actual API keys)
- ❌ `backend/reports/*.pdf` (generated reports)
- ❌ `node_modules/` (large, auto-generated)
- ❌ `venv/` (Python virtual environment)
- ❌ Any files with actual API keys or tokens

---

**Built with ❤️ for the crypto community**

*Disclaimer: This tool is for research and educational purposes only. Not financial advice. Always DYOR (Do Your Own Research).*

## 💰 Cost Estimate

**Free Tier Usage:**
- OpenRouter: $1 free credit = ~650 analyses
- CoinGecko: 30 calls/min = unlimited for personal use
- Twitter: 500k tweets/month (free)
- GitHub: 5000 requests/hour (free with token)

**Paid Usage (after free credits):**
- ~$0.0015 per analysis with GPT-3.5-turbo
- ~$0.15 for 100 analyses
- Can use completely free models if needed!

## 🎓 Learning Resources

New to crypto analysis? Check out:
- Documentation files in the root directory
- API documentation at `/docs` endpoint
- Example API calls in this README
- Showcase feature (20+ pre-analyzed projects)
