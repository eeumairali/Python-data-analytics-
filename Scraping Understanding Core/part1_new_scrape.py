import requests
import re


url = "https://www.dawn.com/news/1945844/have-never-apologised-to-bcci-nor-will-i-mohsin-naqvi-hits-back-at-indian-media-reports"
response = requests.get(url)
data = response.text

# i need h2 tags with re
h2_tags = re.findall(r'<h2.*?>(.*?)</h2>', data, re.DOTALL)

for i, tag in enumerate(h2_tags, 1):
    print(f"H2 Tag {i}: {tag.strip()}")


## you collect and clean data using regular expressions libraries