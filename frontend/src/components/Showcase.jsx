import React, { useState, useEffect } from 'react'
import { TrendingUp, Search } from 'lucide-react'

export default function Showcase({ onSelectProject }) {
  const [projects, setProjects] = useState([])
  const [loading, setLoading] = useState(true)
  const [filter, setFilter] = useState('all')

  useEffect(() => {
    fetchShowcaseProjects()
  }, [])

  const fetchShowcaseProjects = async () => {
    try {
      const response = await fetch('http://localhost:8000/api/v1/showcase')
      const data = await response.json()
      setProjects(data)
    } catch (error) {
      console.error('Error fetching showcase:', error)
    } finally {
      setLoading(false)
    }
  }

  const categories = ['all', ...new Set(projects.map(p => p.category))]
  const filteredProjects = filter === 'all' 
    ? projects 
    : projects.filter(p => p.category === filter)

  if (loading) {
    return (
      <div className="text-center text-white text-xl">Loading showcase projects...</div>
    )
  }

  return (
    <div className="max-w-7xl mx-auto">
      <div className="text-center mb-12">
        <h1 className="text-4xl font-bold text-white mb-4">Project Showcase</h1>
        <p className="text-white/80 text-lg">
          20+ Pre-analyzed crypto projects with AI-powered insights
        </p>
      </div>

      {/* Category Filter */}
      <div className="flex flex-wrap gap-3 justify-center mb-8">
        {categories.map((category) => (
          <button
            key={category}
            onClick={() => setFilter(category)}
            className={`px-6 py-2 rounded-lg font-semibold transition-all ${
              filter === category
                ? 'bg-white text-purple-600'
                : 'bg-white/20 text-white hover:bg-white/30'
            }`}
          >
            {category.charAt(0).toUpperCase() + category.slice(1)}
          </button>
        ))}
      </div>

      {/* Projects Grid */}
      <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
        {filteredProjects.map((project, index) => (
          <ProjectCard
            key={index}
            project={project}
            onSelect={() => onSelectProject(project.name)}
          />
        ))}
      </div>
    </div>
  )
}

function ProjectCard({ project, onSelect }) {
  const getRiskColor = (risk) => {
    switch (risk) {
      case 'green': return 'bg-green-500'
      case 'yellow': return 'bg-yellow-500'
      case 'red': return 'bg-red-500'
      default: return 'bg-gray-500'
    }
  }

  const getScoreGradient = (score) => {
    if (score >= 40) return 'from-green-400 to-green-600'
    if (score >= 30) return 'from-yellow-400 to-yellow-600'
    return 'from-orange-400 to-orange-600'
  }

  return (
    <div className="bg-white rounded-xl shadow-xl overflow-hidden hover:shadow-2xl transition-all transform hover:-translate-y-1">
      <div className={`h-2 bg-gradient-to-r ${getScoreGradient(project.score)}`}></div>
      
      <div className="p-6">
        <div className="flex items-start justify-between mb-4">
          <div>
            <h3 className="text-xl font-bold text-gray-800">{project.name}</h3>
            <p className="text-gray-500">${project.symbol}</p>
          </div>
          <div className={`w-3 h-3 rounded-full ${getRiskColor(project.risk)}`}></div>
        </div>

        <div className="flex items-center justify-between mb-4">
          <div>
            <div className="text-sm text-gray-500">Score</div>
            <div className="text-2xl font-bold text-gray-800">{project.score}/50</div>
          </div>
          <div className="text-right">
            <div className="text-sm text-gray-500">Category</div>
            <div className="text-sm font-semibold text-gray-700">{project.category}</div>
          </div>
        </div>

        <button
          onClick={onSelect}
          className="w-full px-4 py-2 bg-gradient-to-r from-blue-500 to-purple-600 text-white rounded-lg font-semibold hover:shadow-lg transition-all flex items-center justify-center space-x-2"
        >
          <Search className="w-4 h-4" />
          <span>Analyze Now</span>
        </button>
      </div>
    </div>
  )
}
