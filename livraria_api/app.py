from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import banco

app = Flask(__name__)
CORS(app, origins="*")

@app.route("/api/v1/livros", methods=["POST"])
@cross_origin()
def cadastra_novo_livro():
    livro = request.json
    try:
        #validacao de negocio
        banco.insere_livro(livro)
    except Exception as erro:
        print(erro)
        return {"info": "livro incompleto", 'status': 404}, 404

    return f"/api/v1/livros/{livro['id']}", 201


        
app.run(debug=True)

