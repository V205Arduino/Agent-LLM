import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

import requests
from bs4 import BeautifulSoup
load_dotenv()

def find_phrase(url, phrases, num_chars=200):
    try:
        # Send a GET request to the URL
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
        response = requests.get(url, headers=headers)

        # Check if the GET request was successful
        if response.status_code != 200:
            print("Failed to retrieve the webpage. Status code: ", response.status_code)
            return []

        # Parse the HTML content using Beautiful Soup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Remove all script and style elements
        for script in soup(["script", "style"]):
            script.decompose()

        # Get the text from the HTML content
        text = soup.get_text()

        # Break the text into lines and remove leading and trailing whitespace
        lines = (line.strip() for line in text.splitlines())

        # Break multi-headlines into a line each
        chunks = [phrase.strip() for line in lines for phrase in line.split("  ")]

        # Find all occurrences of the phrase and get the surrounding text

        occurrences = []
        for phrase in phrases:
            for chunk in chunks:
                if phrase.lower() in chunk.lower():
                    start_index = chunk.lower().find(phrase.lower())
                    end_index = start_index + len(phrase)
                    start = max(0, start_index - num_chars)
                    end = min(len(chunk), end_index + num_chars)
                    occurrences.append((phrase, chunk[start:end]))

        return occurrences

    except Exception as e:
        print("An error occurred: ", str(e))
        return []
    
    


def get_google_search_results(query, num_results=10):
  
  api_key = os.getenv('SEARCH_API_KEY')
  cx = os.getenv('SEARCH_CX')

  service = build("customsearch", "v1", developerKey=api_key)

  res = service.cse().list(q=query, cx=cx, num=num_results).execute()

  return res['items']











