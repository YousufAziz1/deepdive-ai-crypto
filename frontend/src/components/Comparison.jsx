import React, { useState } from 'react'
import { Plus, X, BarChart3, Download } from 'lucide-react'

export default function Comparison() {
  const [projects, setProjects] = useState(['', '', ''])
  const [comparisonData, setComparisonData] = useState(null)
  const [loading, setLoading] = useState(false)

  const handleProjectChange = (index, value) => {
    const newProjects = [...projects]
    newProjects[index] = value
    setProjects(newProjects)
  }

  const handleCompare = async () => {
    const validProjects = projects.filter(p => p.trim() !== '')
    
    if (validProjects.length < 2) {
      alert('Please enter at least 2 projects to compare')
      return
    }

    setLoading(true)
    
    try {
      const response = await fetch('http://localhost:8000/api/v1/compare', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          projects: validProjects,
        }),
      })

      if (!response.ok) {
        throw new Error('Comparison failed')
      }

      const data = await response.json()
      setComparisonData(data)
    } catch (error) {
      console.error('Error:', error)
      alert('Comparison failed. Please try again.')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="max-w-6xl mx-auto">
      <div className="text-center mb-12">
        <h1 className="text-4xl font-bold text-white mb-4">Compare Projects</h1>
        <p className="text-white/80 text-lg">
          Side-by-side analysis of up to 3 crypto projects
        </p>
      </div>

      <div className="bg-white rounded-2xl shadow-2xl p-8 mb-8">
        <h2 className="text-2xl font-bold text-gray-800 mb-6">Select Projects to Compare</h2>
        
        <div className="space-y-4 mb-6">
          {projects.map((project, index) => (
            <div key={index} className="flex items-center space-x-4">
              <div className="flex-1">
                <input
                  type="text"
                  value={project}
                  onChange={(e) => handleProjectChange(index, e.target.value)}
                  placeholder={`Project ${index + 1} name...`}
                  className="w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:outline-none focus:border-blue-500"
                />
              </div>
            </div>
          ))}
        </div>

        <button
          onClick={handleCompare}
          disabled={loading || projects.filter(p => p.trim()).length < 2}
          className="w-full px-6 py-4 bg-gradient-to-r from-blue-500 to-purple-600 text-white rounded-xl font-semibold hover:shadow-xl transition-all disabled:opacity-50 flex items-center justify-center space-x-2"
        >
          <BarChart3 className="w-5 h-5" />
          <span>{loading ? 'Comparing...' : 'Compare Projects'}</span>
        </button>
      </div>

      {comparisonData && (
        <div className="bg-white rounded-2xl shadow-2xl p-8">
          <h2 className="text-2xl font-bold text-gray-800 mb-6">Comparison Results</h2>
          <div className="grid grid-cols-3 gap-6">
            {comparisonData.projects.map((project, index) => (
              <div key={index} className="text-center">
                <h3 className="font-bold text-xl mb-2">{project.project_data.project_name}</h3>
                <div className="text-3xl font-bold text-blue-600">{project.scores.total}/50</div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  )
}

function formatLargeNumber(num) {
  if (!num) return 'N/A'
  if (num >= 1e9) return `$${(num / 1e9).toFixed(2)}B`
  if (num >= 1e6) return `$${(num / 1e6).toFixed(2)}M`
  return `$${num.toFixed(2)}`
}
