#1
from bs4 import BeautifulSoup
#2
import urllib.request       
#3
soup = BeautifulSoup('<b id="bTag1" class="boldest">Extremely bold</b>',"html.parser")
#4
tag = soup.b
#5
print(tag['class'])

