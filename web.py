from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import os   

app = Flask(__name__)

#Criar GetByID: http://blog.luisrei.com/articles/flaskrest.html

@app.route('/api/v1/filmes', methods=['GET'])
def filmes():
    html_doc = urlopen("http://www.adorocinema.com/filmes/numero-cinemas/").read()
    soup = BeautifulSoup(html_doc, "html.parser")

    data = []
    for dataBox in soup.find_all("div",class_="data_box"):
        nomeObj = dataBox.find("h2", class_="tt_18 d_inline").find("a", class_="no_underline")
        imgObj = dataBox.find(class_="img_side_content")
        sinopseObj = dataBox.find("div", class_="content").find("p")
        dataObj = dataBox.find("ul", class_="list_item_p2v tab_col_first").find("div", class_="oflow_a")

        data.append({ 'nome': nomeObj.text.strip(),
                  'poster' : imgObj.img['src'].strip(),
                  'sinopse' : sinopseObj.text.strip(),
                  'data' :  dataObj.text.strip()})
                
    return jsonify({'filmes': data})

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    # Tem que ser 0.0.0.0 para rodar no Heroku
    app.run(host='0.0.0.0', port=port)