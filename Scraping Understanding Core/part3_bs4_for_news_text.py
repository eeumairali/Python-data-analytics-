import requests
from bs4 import BeautifulSoup

url = "https://www.dawn.com/news/1945844/have-never-apologised-to-bcci-nor-will-i-mohsin-naqvi-hits-back-at-indian-media-reports"
response = requests.get(url)
data = response.text

soup = BeautifulSoup(data, 'html.parser')


text_article = soup.findAll('div', class_='story__content')
for i, tag in enumerate(text_article, 1):
    print(f"Article Text {i}: {tag.get_text(strip=True)}")
    print("\n")