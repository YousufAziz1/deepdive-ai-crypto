# DeepDive AI - Complete File Structure

## 📁 Project Layout

```
deepdive-ai/
│
├── 📄 README.md                    # Main project documentation
├── 📄 QUICKSTART.md                # 5-minute setup guide
├── 📄 SETUP_GUIDE.md               # Detailed setup instructions
├── 📄 API_DOCUMENTATION.md         # Complete API reference
├── 📄 DEMO_GUIDE.md                # Presentation and demo guide
├── 📄 PROJECT_SUMMARY.md           # Project overview and status
├── 📄 FILE_STRUCTURE.md            # This file
├── 📄 LICENSE                      # MIT License
├── 📄 .gitignore                   # Git ignore rules
│
├── 🚀 start-backend.bat            # Windows script to start backend
├── 🚀 start-frontend.bat           # Windows script to start frontend
│
├── 📂 backend/                     # Python FastAPI Backend
│   │
│   ├── 📄 main.py                  # FastAPI application entry point
│   ├── 📄 config.py                # Configuration and settings
│   ├── 📄 requirements.txt         # Python dependencies
│   ├── 📄 .env.example             # Environment variables template
│   ├── 📄 .env                     # Your API keys (create this, not in git)
│   │
│   ├── 📂 models/                  # Data models
│   │   ├── __init__.py
│   │   └── schemas.py              # Pydantic schemas for request/response
│   │
│   ├── 📂 routers/                 # API route handlers
│   │   ├── __init__.py
│   │   ├── analysis.py             # /analyze, /compare, /quick-score
│   │   ├── projects.py             # /showcase, /watchlist
│   │   └── reports.py              # /reports endpoints
│   │
│   ├── 📂 services/                # Business logic and external APIs
│   │   ├── __init__.py
│   │   ├── aggregation_service.py  # Main orchestrator for data aggregation
│   │   ├── coingecko_service.py    # CoinGecko API integration
│   │   ├── defillama_service.py    # DefiLlama API integration
│   │   ├── github_service.py       # GitHub API integration
│   │   ├── twitter_service.py      # Twitter API integration
│   │   ├── roma_service.py         # Sentient ROMA AI integration
│   │   └── report_service.py       # PDF report generation
│   │
│   ├── 📂 reports/                 # Generated PDF reports (auto-created)
│   │   └── *.pdf                   # PDF files generated after analysis
│   │
│   └── 📄 showcase_projects.json   # Cached showcase projects data
│
└── 📂 frontend/                    # React Frontend
    │
    ├── 📄 package.json             # Node.js dependencies
    ├── 📄 vite.config.js           # Vite build configuration
    ├── 📄 tailwind.config.js       # TailwindCSS configuration
    ├── 📄 postcss.config.js        # PostCSS configuration
    ├── 📄 index.html               # HTML entry point
    │
    ├── 📂 src/                     # Source code
    │   ├── 📄 main.jsx             # React entry point
    │   ├── 📄 App.jsx              # Main application component
    │   ├── 📄 index.css            # Global styles and Tailwind imports
    │   │
    │   └── 📂 components/          # React components
    │       ├── Header.jsx          # Navigation header
    │       ├── SearchBar.jsx       # Search input with examples
    │       ├── AnalysisResults.jsx # Results display page
    │       ├── Showcase.jsx        # Project showcase library
    │       └── Comparison.jsx      # Project comparison tool
    │
    ├── 📂 node_modules/            # Node.js packages (auto-generated)
    └── 📂 dist/                    # Production build (created by npm run build)
```

## 📊 File Descriptions

### Root Level

| File | Purpose |
|------|---------|
| **README.md** | Main project overview, features, tech stack |
| **QUICKSTART.md** | Get started in 5 minutes |
| **SETUP_GUIDE.md** | Comprehensive setup instructions |
| **API_DOCUMENTATION.md** | Complete API endpoint reference |
| **DEMO_GUIDE.md** | How to demo the application |
| **PROJECT_SUMMARY.md** | Deliverables and project status |
| **LICENSE** | MIT License text |
| **.gitignore** | Files to exclude from git |
| **start-backend.bat** | Quick start script for Windows (backend) |
| **start-frontend.bat** | Quick start script for Windows (frontend) |

### Backend Files

#### Core Files
| File | Lines | Purpose |
|------|-------|---------|
| **main.py** | ~80 | FastAPI app initialization, CORS, routes |
| **config.py** | ~30 | Settings class with environment variables |
| **requirements.txt** | ~17 | Python package dependencies |

#### Models
| File | Lines | Purpose |
|------|-------|---------|
| **models/schemas.py** | ~150 | Pydantic models for data validation |

#### Routers
| File | Lines | Purpose |
|------|-------|---------|
| **routers/analysis.py** | ~100 | Analyze, compare, quick-score endpoints |
| **routers/projects.py** | ~120 | Showcase and watchlist management |
| **routers/reports.py** | ~70 | Report listing and download |

#### Services (Business Logic)
| File | Lines | Purpose |
|------|-------|---------|
| **services/aggregation_service.py** | ~180 | Main orchestration, combines all data sources |
| **services/coingecko_service.py** | ~120 | Fetch token metrics and tokenomics |
| **services/defillama_service.py** | ~90 | Fetch DeFi TVL and protocol data |
| **services/github_service.py** | ~110 | Fetch repository and developer metrics |
| **services/twitter_service.py** | ~130 | Fetch social metrics and sentiment |
| **services/roma_service.py** | ~250 | AI analysis using Sentient ROMA API |
| **services/report_service.py** | ~200 | Generate professional PDF reports |

### Frontend Files

#### Configuration
| File | Purpose |
|------|---------|
| **package.json** | Node.js dependencies and scripts |
| **vite.config.js** | Vite dev server and proxy configuration |
| **tailwind.config.js** | TailwindCSS theme and colors |
| **postcss.config.js** | PostCSS plugins (Tailwind, Autoprefixer) |
| **index.html** | HTML shell for React app |

#### Source Code
| File | Lines | Purpose |
|------|-------|---------|
| **src/main.jsx** | ~10 | React app mounting |
| **src/App.jsx** | ~150 | Main app logic, routing, state management |
| **src/index.css** | ~40 | Global styles and Tailwind directives |

#### Components
| File | Lines | Purpose |
|------|-------|---------|
| **components/Header.jsx** | ~60 | Top navigation bar |
| **components/SearchBar.jsx** | ~60 | Search input with loading states |
| **components/AnalysisResults.jsx** | ~250 | Comprehensive results display |
| **components/Showcase.jsx** | ~120 | Project library with filtering |
| **components/Comparison.jsx** | ~150 | Side-by-side project comparison |

## 🎯 Key Directories

### `/backend/services/`
**Purpose**: Core business logic and external API integrations  
**Most Important Files**:
- `aggregation_service.py` - Orchestrates all data fetching
- `roma_service.py` - AI analysis engine
- `report_service.py` - PDF generation

### `/frontend/src/components/`
**Purpose**: React UI components  
**Most Important Files**:
- `AnalysisResults.jsx` - Main results page (biggest component)
- `App.jsx` - Application shell and routing

### `/backend/routers/`
**Purpose**: API endpoint definitions  
**Pattern**: Each router handles related endpoints

## 📝 Important Files to Modify

### For Customization

**Branding/Styling:**
- `frontend/src/index.css` - Colors, fonts
- `frontend/tailwind.config.js` - Theme colors
- `backend/services/report_service.py` - PDF styling

**Business Logic:**
- `backend/services/roma_service.py` - Scoring algorithm
- `backend/services/aggregation_service.py` - Data sources

**Configuration:**
- `backend/config.py` - Server settings
- `backend/.env` - API keys (never commit!)

## 🔒 Files NOT in Git

These files are excluded via `.gitignore`:

```
backend/.env                    # Your API keys
backend/reports/*.pdf           # Generated reports
backend/showcase_projects.json  # Cached data
backend/venv/                   # Python virtual environment
backend/__pycache__/            # Python cache
frontend/node_modules/          # Node packages
frontend/dist/                  # Production build
```

## 📦 Auto-Generated Files

These are created automatically:

**Backend:**
- `backend/venv/` - Created by `python -m venv venv`
- `backend/__pycache__/` - Python bytecode cache
- `backend/reports/` - Created when first PDF generated

**Frontend:**
- `frontend/node_modules/` - Created by `npm install`
- `frontend/dist/` - Created by `npm run build`

## 🎨 File Size Overview

| Category | Files | Total Lines |
|----------|-------|-------------|
| Backend Python | 15 | ~2,500 |
| Frontend React | 12 | ~1,800 |
| Documentation | 7 | ~3,000 |
| Configuration | 8 | ~300 |
| **Total** | **42** | **~7,600** |

## 🚀 Essential Files for Running

Minimum files needed to run the app:

**Backend Must-Haves:**
1. `backend/main.py`
2. `backend/config.py`
3. `backend/.env` (with API keys)
4. `backend/requirements.txt`
5. All files in `services/`, `routers/`, `models/`

**Frontend Must-Haves:**
1. `frontend/package.json`
2. `frontend/index.html`
3. `frontend/vite.config.js`
4. All files in `src/`

## 📖 Documentation Files

| File | When to Read |
|------|-------------|
| **QUICKSTART.md** | First time setup |
| **SETUP_GUIDE.md** | Detailed installation |
| **README.md** | Project overview |
| **API_DOCUMENTATION.md** | API integration |
| **DEMO_GUIDE.md** | Before presenting |
| **PROJECT_SUMMARY.md** | Understanding scope |

## 🔍 Finding Things

**Need to modify API endpoints?**
→ `backend/routers/`

**Need to change how data is fetched?**
→ `backend/services/`

**Need to update UI?**
→ `frontend/src/components/`

**Need to adjust AI analysis?**
→ `backend/services/roma_service.py`

**Need to customize reports?**
→ `backend/services/report_service.py`

**Need to add API keys?**
→ `backend/.env`

## ✅ Verification Checklist

After setup, you should have:

```
✅ backend/.env (with your API keys)
✅ backend/venv/ (virtual environment)
✅ backend/reports/ (empty folder, auto-created)
✅ frontend/node_modules/ (after npm install)
✅ All files as shown in structure above
```

## 📞 Support

If you're missing files or confused about structure, see:
- **SETUP_GUIDE.md** for troubleshooting
- **QUICKSTART.md** for quick fixes

---

**Total Project Size**: ~7,600 lines across 42 files  
**Installation Time**: ~5 minutes  
**Setup Difficulty**: Beginner-friendly
