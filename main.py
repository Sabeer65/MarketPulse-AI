from langchain_ollama import ChatOllama
from tools import web_search
from database import save_report,get_past_data

llm = ChatOllama(model="llama3.2", temperature=0)

def run_research_mvp(query: str):

    results = get_past_data(query)

    if results['ids'] and results['ids'][0]:
        distance = results['distances'][0][0]
        if distance <0.5:
            return results['documents'][0][0]

    print(f"Scouting the web for {query}")
    raw_data = web_search(query) # Search using duckduckgo in the web for query

    prompt = f"""
    SYSTEM: You are a professional Market Researcher. 
    Every claim you make MUST be followed by the source URL from the search results.
    
    EXAMPLE FORMAT:
    - Revenue is expected to grow by 10% [https://example.com/report123]
    
    DATA: {raw_data}
    
    USER: {query}
    """

    response = llm.invoke(prompt)

    save_report(query, response.content) # Save to chromaDB

    return response.content


if __name__ == "__main__":
    user_input = "Is the outlook for NVIDIA bullish or bearish for late 2026?"
    report = run_research_mvp(user_input)
    print("\n--- MarketPulse Report ---")
    print(report)