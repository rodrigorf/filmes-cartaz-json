Como funciona?
-----------------

1. Acesse o arquivo /web/flask/filmesCartazCinema.py
2. Execute com python e acesse o endereço local no seu PC: http://127.0.0.1:5000/
3. É mostrada a lista em formato JSON com base na URL do site AdoroCinema em: http://www.adorocinema.com/filmes/numero-cinemas/
4. A API pública pode ser visualizada aqui: https://filmespy.herokuapp.com/api/v1/filmes

Estrutura do retorno em JSON
-----------------

[{
	"sinopse": "Em 2029, Logan (Hugh Jackman) ganha a vida como chofer de limousine para cuidar do nonagen\u00e1rio Charles Xavier (Patrick Stewart). Debilitado...",
	"nome": "Logan",
	"data": "02/03/2017\n(2h17min)",
	"poster": "http://br.web.img1.acsta.net/cx_160_213/b_1_d6d6d6/pictures/16/10/05/19/59/363613.jpg"
},

{
	"sinopse": "Moradora de uma pequena aldeia francesa, Bela (Emma Watson) tem o pai capturado pela Fera (Dan Stevens) e decide entregar sua vida ao estranho ser...",
	"nome": "A Bela e a Fera",
	"data": "16/03/2017\n(2h9min)",
	"poster": "http://br.web.img1.acsta.net/cx_160_213/b_1_d6d6d6/pictures/17/01/09/12/22/442219.jpg"
}]



