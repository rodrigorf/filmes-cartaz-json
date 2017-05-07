#PARTE1
from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import os   

#PARTE2
app = Flask(__name__)

#PARTE3
@app.route('/api/v1/filmes', methods=['GET'])
def filmes2():
    #MEU CÒDIGO AQUI
    return "Tudo pronto!"

#PARTE4
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    # Tem que ser 0.0.0.0 para rodar no Heroku
    app.run(host='127.0.0.1', port=port)