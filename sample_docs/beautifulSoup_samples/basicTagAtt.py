from bs4 import BeautifulSoup
import urllib.request       
soup = BeautifulSoup('<b id="bTag1" class="boldest">Extremely bold</b>',"html.parser")
tag = soup.b

print(tag['id'])
print(tag['class'])

