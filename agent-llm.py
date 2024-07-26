import ollama
response = ollama.chat(model='llama3', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])
print(response['message']['content'])

print(ollama.list())


import requests
from bs4 import BeautifulSoup

def search_web(query, num_results=5):
  """Searches the web for a given query and returns the top results.

  Args:
    query: The search query.
    num_results: The number of results to return.

  Returns:
    A list of dictionaries containing the title, link, and snippet of each result.
  """

  url = f"https://www.google.com/search?q={query}"
  headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
  }

  response = requests.get(url, headers=headers)
  soup = BeautifulSoup(response.content, 'html.parser')

  results = []
  for result in soup.select('.tF2Cxc'):
    title = result.select_one('.LC20lb').text
    link = result.select_one('a')['href']
    snippet = result.select_one('.VwiC3b').text

    results.append({
      "title": title,
      "link": link,
      "snippet": snippet
    })

    if len(results) == num_results:
      break

  return results

if __name__ == '__main__':
  query = input("Enter your search query: ")
  results = search_web(query)

  print("\nTop Search Results:")
  for i, result in enumerate(results):
    print(f"{i+1}. {result['title']}")
    print(f"    {result['link']}")
    print(f"    {result['snippet']}\n")