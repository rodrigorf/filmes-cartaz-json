from bs4 import BeautifulSoup
import urllib.request                                       
soup = BeautifulSoup(urllib.request.urlopen("http://google.com").read())

for link in soup.find_all('a'):
    print(link.get('href'))