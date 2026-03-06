from langchain_community.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()

def web_search(query: str):

    results = search_tool.invoke(query)

    return results

if __name__ == "__main__":
    print(web_search("NVIDIA stock bullish"))