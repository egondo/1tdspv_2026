from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)

banco_perguntas = []


@app.route("/api/v1/perguntas", methods=["POST"])
def cadastra_pergunta():
    questao = request.json
    banco_perguntas.append(questao)
    indice = len(banco_perguntas) - 1
    return f"/api/v1/perguntas/{indice}", 201


@app.route("/api/v1/perguntas", methods=["GET"])
def recupera_perguntas():
    return banco_perguntas, 200

@app.route("/api/v1/respostas", methods=["POST"])
def recebe_respostas():
    respostas = request.json
    banco_respostas.append(respostas)
    indice = len(banco_perguntas) - 1
    return f"/api/v1/respostas/{indice}", 201

app.run(debug=True)