import React, { useState } from 'react'
import { Search, Loader2 } from 'lucide-react'

export default function SearchBar({ onSearch, loading }) {
  const [input, setInput] = useState('')

  const handleSubmit = (e) => {
    e.preventDefault()
    if (input.trim()) {
      onSearch(input.trim())
    }
  }

  return (
    <form onSubmit={handleSubmit} className="w-full">
      <div className="relative">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Enter project name, contract address, or @twitter..."
          className="w-full px-6 py-4 pr-32 text-lg rounded-2xl bg-white/95 backdrop-blur-sm shadow-2xl focus:outline-none focus:ring-4 focus:ring-white/50 transition-all"
          disabled={loading}
        />
        <button
          type="submit"
          disabled={loading || !input.trim()}
          className="absolute right-2 top-1/2 -translate-y-1/2 px-6 py-2 bg-gradient-to-r from-blue-500 to-purple-600 text-white rounded-xl font-semibold hover:shadow-lg transition-all disabled:opacity-50 disabled:cursor-not-allowed flex items-center space-x-2"
        >
          {loading ? (
            <>
              <Loader2 className="w-5 h-5 animate-spin" />
              <span>Analyzing...</span>
            </>
          ) : (
            <>
              <Search className="w-5 h-5" />
              <span>Analyze</span>
            </>
          )}
        </button>
      </div>

      <div className="mt-4 flex flex-wrap gap-2 justify-center">
        <span className="text-white/70 text-sm">Try:</span>
        {['Ethereum', 'Render', '$LINK', '0x...', '@uniswap'].map((example) => (
          <button
            key={example}
            type="button"
            onClick={() => setInput(example)}
            className="px-3 py-1 bg-white/10 text-white/90 rounded-lg text-sm hover:bg-white/20 transition-all"
          >
            {example}
          </button>
        ))}
      </div>
    </form>
  )
}
