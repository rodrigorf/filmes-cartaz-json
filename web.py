from flask import Flask, jsonify, request, redirect
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
#from urllib2 import urlopen
import os   

app = Flask(__name__)

#Criar GetByID: http://blog.luisrei.com/articles/flaskrest.html

@app.route('/')
def filmes_home():
    return "Welcome to home"
    
@app.route('/api/v1/filmes/', methods=['GET'])
def filmes_api():
    
    url = "http://www.adorocinema.com/filmes/numero-cinemas/"
    
    html_doc = urlopen(url).read()
    soup = BeautifulSoup(html_doc, "html.parser")

    data = []
    for dataBox in soup.find_all("div", class_="card card-entity card-entity-list cf"):
        nomeObj = dataBox.find("h2", class_="meta-title")
        imgObj = dataBox.find(class_="thumbnail ")
        sinopseObj = dataBox.find("div", class_="synopsis")
        dataObj = dataBox.find(class_="meta-body").find(class_="meta-body-item meta-body-info")

        data.append({   'nome': nomeObj.text.strip(),
                        'poster' : imgObj.img['data-src'].strip(),
                        'sinopse' : sinopseObj.text.strip(),
                        'data' :  dataObj.text[1:23].strip().replace('/',' ')})
                
    return jsonify({'filmes': data})
    
@app.route('/api/v1/filmes/<page_id>')
def filmes_api_page(page_id):
    
    if int(page_id) > 6:
        return redirect("http://python--bergpb.c9users.io/api/v1/filmes", code=200)
        
    else:
        url = "http://www.adorocinema.com/filmes/numero-cinemas/?page={}".format(page_id)
        
        html_doc = urlopen(url).read()
        soup = BeautifulSoup(html_doc, "html.parser")
    
        data = []
        for dataBox in soup.find_all("div", class_="card card-entity card-entity-list cf"):
            nomeObj = dataBox.find("h2", class_="meta-title")
            imgObj = dataBox.find(class_="thumbnail ")
            sinopseObj = dataBox.find("div", class_="synopsis")
            dataObj = dataBox.find(class_="meta-body").find(class_="meta-body-item meta-body-info")
    
            data.append({   'nome': nomeObj.text.strip(),
                            'poster' : imgObj.img['data-src'].strip(),
                            'sinopse' : sinopseObj.text.strip(),
                            'data' :  dataObj.text[1:23].strip().replace('/',' ')})
                    
        return jsonify({'filmes': data})

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    # Tem que ser 0.0.0.0 para rodar no Heroku
    app.run(debug=True, host='0.0.0.0', port=port)
