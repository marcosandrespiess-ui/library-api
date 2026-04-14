from flask import Flask, jsonify, request

app = Flask(__name__)

livros = []
proximo_id = 1

@app.route("/livros", methods=["GET"])
def listar_livros():
    return jsonify(livros)

@app.route("/livros/<int:id>", methods=["GET"])
def buscar_livro(id):
    livro = next((l for l in livros if l["id"] == id), None)
    if livro is None:
        return jsonify({"erro": "Livro não encontrado"}), 404
    return jsonify(livro)

@app.route("/livros", methods=["POST"])
def cadastrar_livro():
    global proximo_id
    dados = request.get_json()
    livro = {
        "id": proximo_id,
        "titulo": dados["titulo"],
        "autor": dados["autor"],
        "ano": dados["ano"],
        "genero": dados["genero"],
        "paginas": dados["paginas"],
        "editora": dados["editora"],
        "edicao": dados["edicao"]
    }
    livros.append(livro)
    proximo_id += 1
    return jsonify(livro), 201

@app.route("/livros/<int:id>", methods=["PUT"])
def atualizar_livro(id):
    livro = next((l for l in livros if l["id"] == id), None)
    if livro is None:
        return jsonify({"erro": "Livro não encontrado"}), 404
    dados = request.get_json()
    livro.update(dados)
    return jsonify(livro)

@app.route("/livros/<int:id>", methods=["DELETE"])
def deletar_livro(id):
    global livros
    livro = next((l for l in livros if l["id"] == id), None)
    if livro is None:
        return jsonify({"erro": "Livro não encontrado"}), 404
    livros = [l for l in livros if l["id"] != id]
    return jsonify({"mensagem": "Livro removido com sucesso"})

if __name__ == "__main__":
    app.run(debug=True)