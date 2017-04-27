from bs4 import BeautifulSoup
import urllib.request                                       
html = urllib.request.urlopen("file:///C:/Users/Rodrigo/Desktop/helloWordPy/emcartazUnico.html").read()
soup = BeautifulSoup(html, "html.parser")

#RETORNA NOME DO FILME
resp = soup.find("h2", class_="tt_18 d_inline").find("a", class_="no_underline")
print("Nome: " + resp.text.strip())

#RETORNA IMAGEM
resp = soup.find(class_="img_side_content")
print("Imagem: " + resp.img['src'].strip())

#RETORNA SINOPSE
resp = soup.find("div", class_="content").find("p")
print("Sinopse: " + resp.text.strip())

#RETORNA DATA LANÇAMENTO
resp = soup.find("ul", class_="list_item_p2v tab_col_first").find("div", class_="oflow_a")
print("Data lancamento: " + resp.text.strip())