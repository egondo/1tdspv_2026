from flask import Flask, jsonify, request
import service
import traceback

app = Flask(__name__)

#partida = {
#    "mandante": "Vasco da Gama",
#    "visitante": "Cruzeiro",
#    "placar_m": 2,
#    "placar_v": 1
#}

@app.route("/api/v1/partidas", methods=["POST"])
def cadastra_partida():
    try:
        partida = request.json
        service.cadastra_partida(partida)
        resp = {"title": "Partida cadastrada com sucesso", "status": 201}
        return resp, 201
    except Exception as erro:
        traceback.print_exc
        resp = {"title": "Erro no cadastro", "status": 404}
        return resp, 404

@app.route("/api/v1/times", methods=["GET"])    
def recupera_times():
    times = service.recupera_times()
    return times, 200

app.run(debug=True)