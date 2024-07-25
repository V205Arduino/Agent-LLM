import googlesearch

def search_web(query, num_results=5):
    """
    Search the web using Google and return top results.

    Args:
        query (str): Search query
        num_results (int, optional): Number of results to return (default: 5)

    Returns:
        list of str: Top search result URLs
    """
    results = []
    for result in googlesearch.search_web(query, num_results=num_results, stop=num_results):
        results.append(result)
    return results
googlesearch.search_web

def print_results(results):
    """Print search results with indexing"""
    for i, result in enumerate(results, start=1):
        print(f"**{i}.** {result}")

def main():
    query = input("Enter your search query: ")
    num_results = int(input("Number of results to show (default: 5): ") or 5)
    results = search_web(query, num_results)
    print(f"\nTop {num_results} results for '{query}':")
    print_results(results)

if __name__ == "__main__":
    main()