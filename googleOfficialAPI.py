#YES THIS WORKS


import os
from dotenv import load_dotenv


load_dotenv()

#MY_ENV_VAR = os.getenv('MY_ENV_VAR')

from googleapiclient.discovery import build

print(os.getenv('SEARCH_CX'))
print(os.getenv('SEARCH_API_KEY'))
def get_google_search_results(query, num_results=10):
  
  api_key = os.getenv('SEARCH_API_KEY')
  cx = os.getenv('SEARCH_CX')

  service = build("customsearch", "v1", developerKey=api_key)

  res = service.cse().list(q=query, cx=cx, num=num_results).execute()

  return res['items']

if __name__ == "__main__":
  search_query = input("Enter your search query: ")
  results = get_google_search_results(search_query)

  for result in results:
    print(f"Title: {result['title']}")
    print(f"Link: {result['link']}")
    print(f"Snippet: {result['snippet']}\n")
