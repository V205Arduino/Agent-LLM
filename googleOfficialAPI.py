#YES THIS WORKS
'''
<script async src="https://cse.google.com/cse.js?cx=722815c0c7b964e2e">
</script>
<div class="gcse-search"></div>
'''

import os
#from dotenv import load_dotenv

#load_dotenv()

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