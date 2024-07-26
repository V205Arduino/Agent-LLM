import requests
from bs4 import BeautifulSoup
 
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
 
URL = "https://google.com"
page = requests.get(URL, headers=headers)



soup = BeautifulSoup(page.content, "html.parser")

print(soup.text)

