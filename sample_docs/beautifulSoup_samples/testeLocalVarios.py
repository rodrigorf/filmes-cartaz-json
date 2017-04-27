from bs4 import BeautifulSoup
import urllib.request                                       
html = urllib.request.urlopen("file:///C:/Users/Rodrigo/Desktop/helloWordPy/emcartazVarios.html").read()
soup = BeautifulSoup(html, "html.parser")

#PERCORRE TODOS DATABOX
for dataBox in soup.find_all("div",class_="data_box"):
    #RETORNA NOME DO FILME
    resp = dataBox.find("h2", class_="tt_18 d_inline").find("a", class_="no_underline")
    print("Nome: " + resp.text.strip())

    #RETORNA IMAGEM
    resp = dataBox.find(class_="img_side_content")
    print("Imagem: " + resp.img['src'].strip())

    #RETORNA SINOPSE
    resp = dataBox.find("div", class_="content").find("p")
    print("Sinopse: " + resp.text.strip())

    #RETORNA DATA LANÇAMENTO
    resp = dataBox.find("ul", class_="list_item_p2v tab_col_first").find("div", class_="oflow_a")
    print("Data lancamento: " + resp.text.strip())
    print(" ")
    