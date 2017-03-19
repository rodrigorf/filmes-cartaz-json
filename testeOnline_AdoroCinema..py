from bs4 import BeautifulSoup
import urllib.request      
import html
import json

html_doc = urllib.request.urlopen("http://www.adorocinema.com/filmes/numero-cinemas/").read()
soup = BeautifulSoup(html_doc, "html.parser")
#print(soup.prettify())
#print(html_doc)

data = []

#PERCORRE TODOS DATABOX
for dataBox in soup.find_all("div",class_="data_box"):
    #RETORNA NOME DO FILME
    nomeObj = dataBox.find("h2", class_="tt_18 d_inline").find("a", class_="no_underline")
    #str_pura = "Nega\xc3\xa7\xc3\xa3o"
    #print(str_pura)
    #str_encoded = str.encode(str_pura)
    #print("Nome COM Decode: " + str_encoded.decode())
    #print("Nome: " + nomeObj.text.strip())

    #RETORNA IMAGEM
    imgObj = dataBox.find(class_="img_side_content")
    #print("Poster: " + imgObj.img['src'].strip())

    #RETORNA SINOPSE
    sinopseObj = dataBox.find("div", class_="content").find("p")
    #print("Sinopse: " + sinopseObj.text.strip())

    #RETORNA DATA LANÇAMENTO
    dataObj = dataBox.find("ul", class_="list_item_p2v tab_col_first").find("div", class_="oflow_a")
    #print("Data lancamento: " + dataObj.text.strip())

    data.append({ 'nome': nomeObj.text.strip(),
                  'poster' : imgObj.img['src'].strip(),
                  'sinopse' : sinopseObj.text.strip(),
                  'data' :  dataObj.text.strip()})
    print(" ")
    
json_data = json.dumps(data)
print(json_data)