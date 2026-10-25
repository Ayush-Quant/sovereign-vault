import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def fetch_cognitive_research(query="cognitive ergonomics attention residue focus strategies"):
    try:
        response = tavily_client.search(
            query=query,
            search_depth="basic",
            max_results=2
        )
        results = response.get("results", [])
        snippets = [f"- **{r['title']}**: {r['content']} ({r['url']})" for r in results]
        return "\n".join(snippets) if snippets else "No live research snippets retrieved."
    except Exception as e:
        return f"[!] Tavily Search Error: {e}"

if __name__ == "__main__":
    print("[*] Testing Tavily Live Research Integration...")
    research = fetch_cognitive_research()
    print(f"\n[Retrieved Research]:\n{research}")
