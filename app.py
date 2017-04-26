from flask import Flask, jsonify
from bs4 import BeautifulSoup
import urllib.request      
import html
import json


app = Flask(__name__)

@app.route('/api/v1/filmes', methods=['GET'])
def filmes():
    html_doc = urllib.request.urlopen("http://www.adorocinema.com/filmes/numero-cinemas/").read()
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
                
    # response = app.response_class(
    #     response=json.dumps(data),
    #     status=200,
    #     mimetype='application/json'
    # )
    # return response
    
    return jsonify({'filmes': data})

if __name__ == "__main__":
    app.run(debug=True)