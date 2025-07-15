# search_tool.py
"""
Search tool that uses SerpApi (with API key) or a free Google search fallback.
"""

import os
from typing import Optional

try:
    from serpapi import GoogleSearch
    serpapi_available = True
except ImportError:
    serpapi_available = False

class SearchTool:
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the search tool. Use SerpApi if api_key is given (or in SERPAPI_KEY env).
        Otherwise uses google search scraping.
        """
        self.api_key = api_key or os.getenv("SERPAPI_KEY")
        if self.api_key and not serpapi_available:
            print("Warning: SerpApi key provided but serpapi library not installed.")
    
    def search(self, query: str, num_results: int = 3) -> str:
        """
        Search the web for the query and return a summary of top results.
        """
        # If SerpApi key available, use SerpApi GoogleSearch
        if self.api_key and serpapi_available:
            params = {
                "q": query,
                "num": num_results,
                "api_key": self.api_key
            }
            search = GoogleSearch(params)
            results = search.get_dict()
            # Extract top organic results
            snippets = []
            for res in results.get("organic_results", [])[:num_results]:
                title = res.get("title", "")
                snippet = res.get("snippet", "")
                snippets.append(f"{title}: {snippet}")
            return "\n".join(snippets)
        else:
            # Fallback: use googlesearch to scrape Google
            try:
                from googlesearch import search
            except ImportError:
                return "Search library not available."
            results = []
            for url in search(query, num_results=num_results):
                results.append(url)
            return "\n".join(results)

# Example usage:
# tool = SearchTool(api_key="YOUR_SERPAPI_KEY")
# print(tool.search("Who is the president of the USA?"))
# print(tool.search("coffee shop nearby", num_results=2))
