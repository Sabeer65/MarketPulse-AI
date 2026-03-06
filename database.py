import chromadb

client = chromadb.HttpClient(host='localhost' ,port=8000)

def save_report(topic: str, report_content: str):
    collection = client.get_or_create_collection(name="market_reports")

    collection.add(documents=[report_content],
        metadatas=[{"topic": topic}],
        ids=[topic.replace(" ", "_").lower()] 
    )

    print(f'Report for {topic} saved to long-term memory')

def get_past_data(query: str):
    collection = client.get_or_create_collection(name='market_reports')

    results = collection.query(
        query_texts=[query], 
        n_results=1
    )
    return results
