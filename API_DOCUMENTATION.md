# DeepDive AI - API Documentation

Complete API reference for DeepDive AI Crypto Research Agent.

## Base URL

```
http://localhost:8000/api/v1
```

## Authentication

Currently, the API does not require authentication for local development. In production, implement API key authentication.

---

## Endpoints

### 1. Health Check

Check if the API is running.

**Endpoint**: `GET /`

**Response**:
```json
{
  "status": "healthy",
  "service": "DeepDive AI - Crypto Research Agent",
  "version": "1.0.0"
}
```

---

### 2. Analyze Project

Perform comprehensive AI-powered analysis of a crypto project.

**Endpoint**: `POST /api/v1/analyze`

**Request Body**:
```json
{
  "input": "Ethereum",
  "input_type": "project_name"  // Optional: "project_name", "contract_address", "twitter_handle"
}
```

**Response**:
```json
{
  "project_data": {
    "project_name": "Ethereum",
    "symbol": "ETH",
    "contract_address": null,
    "website": "https://ethereum.org",
    "description": "Ethereum is a decentralized platform...",
    "token_metrics": {
      "price": 2245.67,
      "market_cap": 270000000000,
      "fully_diluted_valuation": 270000000000,
      "volume_24h": 15000000000,
      "holders": 245000000,
      "price_change_24h": 2.5,
      "price_change_7d": 5.8
    },
    "tokenomics": {
      "total_supply": 120000000,
      "circulating_supply": 120000000,
      "max_supply": null,
      "distribution": {},
      "vesting_schedule": null
    },
    "social_metrics": {
      "twitter_followers": 3200000,
      "twitter_engagement_rate": 2.5,
      "sentiment_score": 7.8,
      "recent_mentions": 15000
    },
    "technical_metrics": {
      "github_stars": 42000,
      "github_forks": 18000,
      "commits_last_month": 450,
      "contributors": 800,
      "last_commit_date": "2024-10-17T10:30:00Z"
    },
    "team_info": {
      "members": [],
      "linkedin_profiles": [],
      "past_projects": []
    }
  },
  "executive_summary": "Ethereum is the leading smart contract platform...",
  "scores": {
    "team_credibility": 9,
    "product_market_fit": 10,
    "tokenomics_health": 8,
    "community_strength": 10,
    "technical_development": 9,
    "total": 46
  },
  "risk_flags": {
    "level": "green",
    "flags": []
  },
  "investment_thesis": {
    "bull_case": [
      "Leading smart contract platform",
      "Strong developer ecosystem",
      "Successful merge to PoS"
    ],
    "bear_case": [
      "High gas fees",
      "Competition from other L1s",
      "Regulatory uncertainty"
    ],
    "recommendation": "Strong Buy"
  },
  "report_url": "/reports/Ethereum_20241017_123456.pdf",
  "analysis_timestamp": "2024-10-17T12:34:56.789Z"
}
```

**Status Codes**:
- `200 OK`: Analysis successful
- `400 Bad Request`: Invalid input
- `500 Internal Server Error`: Analysis failed

---

### 3. Compare Projects

Compare 2-3 projects side-by-side.

**Endpoint**: `POST /api/v1/compare`

**Request Body**:
```json
{
  "projects": ["Ethereum", "Solana", "Cardano"]
}
```

**Response**:
```json
{
  "projects": [
    {
      // Full AnalysisResponse object for each project
    }
  ],
  "comparative_summary": "AI-generated comparison summary..."
}
```

**Constraints**:
- Minimum 2 projects
- Maximum 3 projects

**Status Codes**:
- `200 OK`: Comparison successful
- `400 Bad Request`: Invalid number of projects
- `500 Internal Server Error`: Comparison failed

---

### 4. Quick Score

Get a quick score without full analysis.

**Endpoint**: `GET /api/v1/quick-score/{project_name}`

**Example**:
```
GET /api/v1/quick-score/Bitcoin
```

**Response**:
```json
{
  "project_name": "Bitcoin",
  "total_score": 45,
  "risk_level": "green",
  "price": 43250.50,
  "market_cap": 845000000000
}
```

---

### 5. Get Showcase Projects

Retrieve list of pre-analyzed showcase projects.

**Endpoint**: `GET /api/v1/showcase`

**Response**:
```json
[
  {
    "name": "Ethereum",
    "symbol": "ETH",
    "score": 48,
    "risk": "green",
    "category": "Layer 1"
  },
  {
    "name": "Chainlink",
    "symbol": "LINK",
    "score": 45,
    "risk": "green",
    "category": "Oracle"
  }
  // ... more projects
]
```

---

### 6. Add to Showcase

Add a project to the showcase library.

**Endpoint**: `POST /api/v1/showcase`

**Request Body**:
```json
{
  "name": "Render",
  "symbol": "RNDR",
  "score": 42,
  "risk": "green",
  "category": "Infrastructure"
}
```

**Response**:
```json
{
  "status": "success",
  "message": "Project added to showcase"
}
```

---

### 7. List Reports

Get list of all generated PDF reports.

**Endpoint**: `GET /api/v1/reports`

**Response**:
```json
[
  "Ethereum_20241017_123456.pdf",
  "Bitcoin_20241017_120000.pdf",
  "comparison_20241017_115000.pdf"
]
```

---

### 8. Download Report

Download a specific PDF report.

**Endpoint**: `GET /api/v1/reports/{filename}`

**Example**:
```
GET /api/v1/reports/Ethereum_20241017_123456.pdf
```

**Response**: PDF file download

**Status Codes**:
- `200 OK`: File found and returned
- `404 Not Found`: Report doesn't exist

---

### 9. Delete Report

Remove a report from storage.

**Endpoint**: `DELETE /api/v1/reports/{filename}`

**Response**:
```json
{
  "status": "success",
  "message": "Report Ethereum_20241017_123456.pdf deleted"
}
```

---

## Data Models

### ProjectData

```typescript
{
  project_name: string
  symbol?: string
  contract_address?: string
  website?: string
  description?: string
  token_metrics: TokenMetrics
  tokenomics: Tokenomics
  social_metrics: SocialMetrics
  technical_metrics: TechnicalMetrics
  team_info: TeamInfo
}
```

### Scores

```typescript
{
  team_credibility: number    // 0-10
  product_market_fit: number  // 0-10
  tokenomics_health: number   // 0-10
  community_strength: number  // 0-10
  technical_development: number // 0-10
  total: number              // 0-50
}
```

### RiskFlags

```typescript
{
  level: "green" | "yellow" | "red"
  flags: string[]
}
```

---

## Rate Limits

### Development
- No rate limits on localhost

### Production (Recommended)
- **Free Tier**: 100 requests/day
- **Pro Tier**: 1000 requests/day
- **Enterprise**: Custom limits

Implement rate limiting using:
```python
from slowapi import Limiter
```

---

## Error Responses

All errors follow this format:

```json
{
  "detail": "Error message here"
}
```

### Common Error Codes

- `400 Bad Request`: Invalid input parameters
- `404 Not Found`: Resource not found
- `429 Too Many Requests`: Rate limit exceeded
- `500 Internal Server Error`: Server-side error
- `503 Service Unavailable`: External API failure

---

## Integration Examples

### Python

```python
import requests

# Analyze a project
response = requests.post(
    "http://localhost:8000/api/v1/analyze",
    json={"input": "Ethereum"}
)
data = response.json()
print(f"Score: {data['scores']['total']}/50")
```

### JavaScript/Node.js

```javascript
const axios = require('axios');

async function analyzeProject(name) {
  const response = await axios.post(
    'http://localhost:8000/api/v1/analyze',
    { input: name }
  );
  return response.data;
}

analyzeProject('Bitcoin').then(data => {
  console.log(`Score: ${data.scores.total}/50`);
});
```

### cURL

```bash
curl -X POST "http://localhost:8000/api/v1/analyze" \
  -H "Content-Type: application/json" \
  -d '{"input": "Chainlink"}'
```

---

## WebSocket Support (Future)

Coming soon: Real-time analysis updates via WebSocket.

```javascript
const ws = new WebSocket('ws://localhost:8000/ws');
ws.onmessage = (event) => {
  const data = JSON.parse(event.data);
  console.log('Analysis update:', data);
};
```

---

## Pagination (Future)

For large result sets:

```
GET /api/v1/showcase?page=1&limit=20
```

---

## Interactive Documentation

Visit `http://localhost:8000/docs` for:
- Interactive API testing
- Request/response examples
- Schema documentation
- Try-it-now functionality

---

## Support

- **Documentation**: Full docs at `/docs`
- **Issues**: GitHub Issues
- **Email**: api-support@deepdive.ai

---

**API Version**: 1.0.0  
**Last Updated**: October 2024
