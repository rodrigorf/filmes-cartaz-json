from bs4 import BeautifulSoup
import urllib.request                                       
#html = urllib.request.urlopen("http://google.com").read()
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html, "html.parser")
#soup = BeautifulSoup('<div id="dvExt" class="frint"><b id="bTag1" class="logo-subtext">Extremely bold</b></div>',"html.parser")
resp = soup.find(class_="story").find(id="link2")

print(resp)

