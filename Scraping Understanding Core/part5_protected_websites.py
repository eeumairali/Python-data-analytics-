import requests

url = "https://www.daraz.pk/products/always-thicks-sanitary-pads-extra-long-trio-26-count-i1302018-s8869425.html?scm=1007.51610.379274.0&pvid=2318753a-8778-4ca9-8608-499959befbe0&search=flashsale&spm=a2a0e.tm80335142.FlashSale.d_1302018"
response = requests.get(url)
data = response.text
print(data)