from bs4 import BeautifulSoup
import urllib.request               

html =  urllib.request.urlopen("http://www.adorocinema.com/filmes/numero-cinemas/").read()
soup = BeautifulSoup(html, "html.parser")
print(html)

#PERCORRE TODOS DATABOX
for dataBox in soup.find_all("div", class_="card card-entity card-entity-list cf hred"):
    #RETORNA NOME DO FILME
    resp = dataBox.find("h2", class_="meta-title")
    print("Nome: " + resp.text.strip())

    #RETORNA IMAGEM !!!!!!!!!!!
    resp = dataBox.find(class_="thumbnail ")
    print("Imagem: " + resp.img['data-src'].strip())

    # #RETORNA SINOPSE
    resp = dataBox.find("div", class_="synopsis")
    print("Sinopse: " + resp.text.strip())

    # #RETORNA DATA LANÇAMENTO
    resp = dataBox.find(class_="meta-body").find(class_="meta-body-item meta-body-info")
    print("Data lancamento: " + resp.text[1:23].strip().replace('/',' '))
    print(" ")
    