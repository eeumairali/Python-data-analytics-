import requests
from bs4 import BeautifulSoup

url = "https://www.dawn.com/news/1945844/have-never-apologised-to-bcci-nor-will-i-mohsin-naqvi-hits-back-at-indian-media-reports"
response = requests.get(url)
data = response.text

soup = BeautifulSoup(data, 'html.parser')
h2_tags = soup.find_all('h2')

for i, tag in enumerate(h2_tags, 1):
    print(f"H2 Tag {i}: {tag.get_text(strip=True)}")
