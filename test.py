from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import os   

URL = "http://www.adorocinema.com/filmes/todos-filmes/notas-espectadores/"
    
html_doc = urlopen(URL).read()
soup = BeautifulSoup(html_doc, "html.parser")
data = []
for dataBox in soup.find_all("div", class_="data_box"):
    content = dataBox.find("div", class_="content")
    print(content.text.strip().split('Gênero')[1][100:])
    