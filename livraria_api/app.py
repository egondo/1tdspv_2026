from flask import Flask, request, jsonify
import db

app = Flask(__name__)


@app.route("/api/v1/hello", methods=["GET"])
def hello():
    dic = {"title": "Hello, minha primeira API python"}
    return dic

@app.route("/api/v1/hello/<msg>", methods=["GET"])
def hello_param(msg: str):
    dic = {"title": msg}
    return dic

@app.route("/api/v1/livros", methods=["GET"])
def get_all():
    return db.livros, 200

@app.route("/api/v1/livros/<int:id>", methods=["GET"])
def get_by_id(id: int):
    for livro in db.livros:
        if livro['id'] == id:
            return livro, 200
    
    resp = {"info": f"Livro {id} não encontrado", 'status': 404}
    return resp, 404

@app.route("/api/v1/livros", methods=["POST"])
def cadastra_novo_livro():
    livro = request.json
    try:
        aux = livro['id']
        aux = livro['titulo']
        aux = livro['autor']
        aux = livro['quantidade']
        aux = livro['categoria']
        aux = livro['valor']
    except Exception as erro:
        return {"info": "livro incompleto", 'status': 404}, 404

    db.livros.append(livro)    
    return f"/api/v1/livros/{livro['id']}", 201


#Definir um método put
@app.route("/api/v1/livros", methods=["PUT"])
def altera_livro(id: int):
    #implemente a logica de alteracao, nao e necessario logica de negocio
    return None

#Definir um método delete
@app.route("/api/v1/livros", methods=["DELETE"])
def apaga_livro(id: int):
    #implemente a logica de alteracao, nao e necessario logica de negocio
    return None


app.run(debug=True)

