import React, { useState } from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Header from './components/Header'
import SearchBar from './components/SearchBar'
import AnalysisResults from './components/AnalysisResults'
import Showcase from './components/Showcase'
import Comparison from './components/Comparison'

function App() {
  const [currentView, setCurrentView] = useState('home')
  const [analysisData, setAnalysisData] = useState(null)
  const [loading, setLoading] = useState(false)

  const handleSearch = async (searchInput) => {
    setLoading(true)
    setAnalysisData(null)

    try {
      const response = await fetch('http://localhost:8000/api/v1/analyze', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          input: searchInput,
        }),
      })

      if (!response.ok) {
        throw new Error('Analysis failed')
      }

      const data = await response.json()
      setAnalysisData(data)
      setCurrentView('results')
    } catch (error) {
      console.error('Error:', error)
      alert('Analysis failed. Please check if the backend is running.')
    } finally {
      setLoading(false)
    }
  }

  return (
    <Router>
      <div className="min-h-screen">
        <Header currentView={currentView} setCurrentView={setCurrentView} />
        
        <main className="container mx-auto px-4 py-8">
          {currentView === 'home' && (
            <div className="max-w-4xl mx-auto">
              <div className="text-center mb-12">
                <h1 className="text-5xl font-bold text-white mb-4">
                  DeepDive AI
                </h1>
                <p className="text-xl text-white/90 mb-2">
                  Crypto Research Agent Powered by ROMA
                </p>
                <p className="text-white/75">
                  Get comprehensive AI-powered analysis in 60 seconds
                </p>
              </div>

              <SearchBar onSearch={handleSearch} loading={loading} />

              <div className="mt-16">
                <h2 className="text-2xl font-bold text-white mb-6 text-center">
                  How It Works
                </h2>
                <div className="grid md:grid-cols-3 gap-8">
                  <FeatureCard
                    title="1. Input Project"
                    description="Enter project name, contract address, or Twitter handle"
                    icon="🔍"
                  />
                  <FeatureCard
                    title="2. AI Analysis"
                    description="ROMA analyzes data from CoinGecko, GitHub, Twitter, and more"
                    icon="🤖"
                  />
                  <FeatureCard
                    title="3. Get Report"
                    description="Receive detailed PDF report with scores and investment thesis"
                    icon="📊"
                  />
                </div>
              </div>
            </div>
          )}

          {currentView === 'results' && analysisData && (
            <AnalysisResults data={analysisData} onBack={() => setCurrentView('home')} />
          )}

          {currentView === 'showcase' && (
            <Showcase onSelectProject={handleSearch} />
          )}

          {currentView === 'comparison' && (
            <Comparison />
          )}
        </main>
      </div>
    </Router>
  )
}

function FeatureCard({ title, description, icon }) {
  return (
    <div className="bg-white/10 backdrop-blur-lg rounded-xl p-6 text-center hover:bg-white/20 transition-all">
      <div className="text-4xl mb-4">{icon}</div>
      <h3 className="text-xl font-bold text-white mb-2">{title}</h3>
      <p className="text-white/80">{description}</p>
    </div>
  )
}

export default App
