import React from 'react'
import { Search, BarChart3, Star } from 'lucide-react'

export default function Header({ currentView, setCurrentView }) {
  return (
    <header className="bg-white/10 backdrop-blur-lg border-b border-white/20">
      <div className="container mx-auto px-4 py-4">
        <div className="flex items-center justify-between">
          <div 
            className="flex items-center space-x-2 cursor-pointer"
            onClick={() => setCurrentView('home')}
          >
            <BarChart3 className="w-8 h-8 text-white" />
            <span className="text-xl font-bold text-white">DeepDive AI</span>
          </div>

          <nav className="flex items-center space-x-6">
            <button
              onClick={() => setCurrentView('home')}
              className={`flex items-center space-x-2 px-4 py-2 rounded-lg transition-all ${
                currentView === 'home'
                  ? 'bg-white/20 text-white'
                  : 'text-white/70 hover:text-white hover:bg-white/10'
              }`}
            >
              <Search className="w-4 h-4" />
              <span>Analyze</span>
            </button>

            <button
              onClick={() => setCurrentView('showcase')}
              className={`flex items-center space-x-2 px-4 py-2 rounded-lg transition-all ${
                currentView === 'showcase'
                  ? 'bg-white/20 text-white'
                  : 'text-white/70 hover:text-white hover:bg-white/10'
              }`}
            >
              <Star className="w-4 h-4" />
              <span>Showcase</span>
            </button>

            <button
              onClick={() => setCurrentView('comparison')}
              className={`flex items-center space-x-2 px-4 py-2 rounded-lg transition-all ${
                currentView === 'comparison'
                  ? 'bg-white/20 text-white'
                  : 'text-white/70 hover:text-white hover:bg-white/10'
              }`}
            >
              <BarChart3 className="w-4 h-4" />
              <span>Compare</span>
            </button>
          </nav>
        </div>
      </div>
    </header>
  )
}
