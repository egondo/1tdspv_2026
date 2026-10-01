from flask import Flask, request, jsonify
import banco

app = Flask(__name__)

@app.route("/api/v1/livros", methods=["POST"])
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

