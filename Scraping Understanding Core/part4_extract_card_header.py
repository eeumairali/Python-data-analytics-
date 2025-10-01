import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news/articles/cy8r2ej4m0ro"
response = requests.get(url)
data = response.text

soup = BeautifulSoup(data, 'html.parser')
# pettern


text_article = soup.findAll('h2', class_='sc-9d830f2a-3')
for i, tag in enumerate(text_article, 1):
    print(f"Header {i}: {tag.get_text(strip=True)}")
    print("\n")