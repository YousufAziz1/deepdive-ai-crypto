import React from 'react'
import { ArrowLeft, Download, ExternalLink, TrendingUp, AlertTriangle, CheckCircle } from 'lucide-react'

export default function AnalysisResults({ data, onBack }) {
  const { project_data, executive_summary, scores, risk_flags, investment_thesis } = data

  const handleDownloadReport = async () => {
    try {
      const response = await fetch('http://localhost:8000/api/v1/generate-report', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      })

      if (!response.ok) {
        throw new Error('Report generation failed')
      }

      const blob = await response.blob()
      const url = window.URL.createObjectURL(blob)
      const a = document.createElement('a')
      a.href = url
      a.download = `${project_data.project_name}_analysis.pdf`
      document.body.appendChild(a)
      a.click()
      window.URL.revokeObjectURL(url)
      document.body.removeChild(a)
    } catch (error) {
      console.error('Error downloading report:', error)
      alert('Failed to download report. Please try again.')
    }
  }

  const getRiskColor = (level) => {
    switch (level) {
      case 'green': return 'text-green-500'
      case 'yellow': return 'text-yellow-500'
      case 'red': return 'text-red-500'
      default: return 'text-gray-500'
    }
  }

  const getScoreColor = (score) => {
    if (score >= 8) return 'bg-green-500'
    if (score >= 6) return 'bg-yellow-500'
    if (score >= 4) return 'bg-orange-500'
    return 'bg-red-500'
  }

  return (
    <div className="max-w-6xl mx-auto">
      <button
        onClick={onBack}
        className="flex items-center space-x-2 text-white/80 hover:text-white mb-6 transition-colors"
      >
        <ArrowLeft className="w-5 h-5" />
        <span>Back to Search</span>
      </button>

      {/* Header Card */}
      <div className="bg-white rounded-2xl shadow-2xl p-8 mb-6">
        <div className="flex items-start justify-between mb-6">
          <div>
            <h1 className="text-4xl font-bold text-gray-800 mb-2">
              {project_data.project_name}
              {project_data.symbol && (
                <span className="text-2xl text-gray-500 ml-3">${project_data.symbol}</span>
              )}
            </h1>
            {project_data.website && (
              <a
                href={project_data.website}
                target="_blank"
                rel="noopener noreferrer"
                className="text-blue-600 hover:underline flex items-center space-x-1"
              >
                <span>{project_data.website}</span>
                <ExternalLink className="w-4 h-4" />
              </a>
            )}
          </div>
          
          <div className="text-right">
            <div className="text-3xl font-bold text-gray-800">
              {scores.total}/50
            </div>
            <div className={`flex items-center justify-end space-x-1 ${getRiskColor(risk_flags.level)}`}>
              <div className="w-3 h-3 rounded-full bg-current"></div>
              <span className="text-sm font-semibold">{risk_flags.level.toUpperCase()}</span>
            </div>
          </div>
        </div>

        {/* Token Metrics */}
        <div className="grid grid-cols-4 gap-4 mb-6">
          <MetricCard
            label="Price"
            value={`$${project_data.token_metrics.price?.toFixed(4) || 'N/A'}`}
          />
          <MetricCard
            label="Market Cap"
            value={formatLargeNumber(project_data.token_metrics.market_cap)}
          />
          <MetricCard
            label="24h Volume"
            value={formatLargeNumber(project_data.token_metrics.volume_24h)}
          />
          <MetricCard
            label="FDV"
            value={formatLargeNumber(project_data.token_metrics.fully_diluted_valuation)}
          />
        </div>

        {/* Executive Summary */}
        <div className="bg-blue-50 rounded-xl p-6">
          <h2 className="text-xl font-bold text-gray-800 mb-3">Executive Summary</h2>
          <p className="text-gray-700 leading-relaxed">{executive_summary}</p>
        </div>
      </div>

      {/* Scores Grid */}
      <div className="grid md:grid-cols-2 gap-6 mb-6">
        <div className="bg-white rounded-2xl shadow-xl p-6">
          <h2 className="text-2xl font-bold text-gray-800 mb-6">Analysis Scores</h2>
          <div className="space-y-4">
            <ScoreBar label="Team Credibility" score={scores.team_credibility} />
            <ScoreBar label="Product-Market Fit" score={scores.product_market_fit} />
            <ScoreBar label="Tokenomics Health" score={scores.tokenomics_health} />
            <ScoreBar label="Community Strength" score={scores.community_strength} />
            <ScoreBar label="Technical Development" score={scores.technical_development} />
          </div>
        </div>

        <div className="bg-white rounded-2xl shadow-xl p-6">
          <h2 className="text-2xl font-bold text-gray-800 mb-6">Risk Assessment</h2>
          <div className="mb-6">
            <div className={`inline-flex items-center space-x-2 px-4 py-2 rounded-lg font-semibold ${
              risk_flags.level === 'green' ? 'bg-green-100 text-green-700' :
              risk_flags.level === 'yellow' ? 'bg-yellow-100 text-yellow-700' :
              'bg-red-100 text-red-700'
            }`}>
              <div className="w-3 h-3 rounded-full bg-current"></div>
              <span>{risk_flags.level.toUpperCase()} RISK</span>
            </div>
          </div>
          
          {risk_flags.flags && risk_flags.flags.length > 0 && (
            <div className="space-y-2">
              <h3 className="font-semibold text-gray-700 mb-3">Risk Flags:</h3>
              {risk_flags.flags.map((flag, index) => (
                <div key={index} className="flex items-start space-x-2 text-gray-600">
                  <AlertTriangle className="w-5 h-5 text-orange-500 mt-0.5 flex-shrink-0" />
                  <span>{flag}</span>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>

      {/* Investment Thesis */}
      <div className="bg-white rounded-2xl shadow-xl p-8 mb-6">
        <h2 className="text-2xl font-bold text-gray-800 mb-6">Investment Thesis</h2>
        
        <div className="grid md:grid-cols-2 gap-8 mb-6">
          <div>
            <h3 className="text-lg font-bold text-green-600 mb-4 flex items-center space-x-2">
              <TrendingUp className="w-5 h-5" />
              <span>Bull Case</span>
            </h3>
            <ul className="space-y-2">
              {investment_thesis.bull_case.map((point, index) => (
                <li key={index} className="flex items-start space-x-2">
                  <CheckCircle className="w-5 h-5 text-green-500 mt-0.5 flex-shrink-0" />
                  <span className="text-gray-700">{point}</span>
                </li>
              ))}
            </ul>
          </div>

          <div>
            <h3 className="text-lg font-bold text-red-600 mb-4 flex items-center space-x-2">
              <AlertTriangle className="w-5 h-5" />
              <span>Bear Case</span>
            </h3>
            <ul className="space-y-2">
              {investment_thesis.bear_case.map((point, index) => (
                <li key={index} className="flex items-start space-x-2">
                  <AlertTriangle className="w-5 h-5 text-red-500 mt-0.5 flex-shrink-0" />
                  <span className="text-gray-700">{point}</span>
                </li>
              ))}
            </ul>
          </div>
        </div>

        <div className="bg-gradient-to-r from-blue-50 to-purple-50 rounded-xl p-6">
          <h3 className="font-bold text-gray-800 mb-2">Recommendation:</h3>
          <p className="text-2xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-purple-600">
            {investment_thesis.recommendation}
          </p>
        </div>
      </div>

      {/* Download Button */}
      <div className="text-center">
        <button 
          onClick={handleDownloadReport}
          className="inline-flex items-center space-x-2 px-8 py-4 bg-gradient-to-r from-blue-500 to-purple-600 text-white rounded-xl font-semibold hover:shadow-2xl transition-all hover:scale-105"
        >
          <Download className="w-5 h-5" />
          <span>Download PDF Report</span>
        </button>
      </div>
    </div>
  )
}

function MetricCard({ label, value }) {
  return (
    <div className="text-center">
      <div className="text-sm text-gray-500 mb-1">{label}</div>
      <div className="text-lg font-bold text-gray-800">{value}</div>
    </div>
  )
}

function ScoreBar({ label, score }) {
  const percentage = (score / 10) * 100
  const getColor = () => {
    if (score >= 8) return 'bg-green-500'
    if (score >= 6) return 'bg-yellow-500'
    if (score >= 4) return 'bg-orange-500'
    return 'bg-red-500'
  }

  return (
    <div>
      <div className="flex justify-between mb-2">
        <span className="text-gray-700 font-medium">{label}</span>
        <span className="font-bold text-gray-800">{score}/10</span>
      </div>
      <div className="w-full bg-gray-200 rounded-full h-3">
        <div
          className={`h-3 rounded-full ${getColor()} transition-all duration-500`}
          style={{ width: `${percentage}%` }}
        ></div>
      </div>
    </div>
  )
}

function formatLargeNumber(num) {
  if (!num) return 'N/A'
  if (num >= 1e9) return `$${(num / 1e9).toFixed(2)}B`
  if (num >= 1e6) return `$${(num / 1e6).toFixed(2)}M`
  if (num >= 1e3) return `$${(num / 1e3).toFixed(2)}K`
  return `$${num.toFixed(2)}`
}
