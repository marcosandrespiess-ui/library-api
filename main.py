from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///livros.db"
db = SQLAlchemy(app)

class Livro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    autor = db.Column(db.String(200), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    genero = db.Column(db.String(100), nullable=False)
    paginas = db.Column(db.Integer, nullable=False)
    editora = db.Column(db.String(200), nullable=False)
    edicao = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "autor": self.autor,
            "ano": self.ano,
            "genero": self.genero,
            "paginas": self.paginas,
            "editora": self.editora,
            "edicao": self.edicao
        }

with app.app_context():
    db.create_all()

@app.route("/livros", methods=["GET"])
def listar_livros():
    livros = Livro.query.all()
    return jsonify([l.to_dict() for l in livros])

@app.route("/livros/<int:id>", methods=["GET"])
def buscar_livro(id):
    livro = Livro.query.get(id)
    if livro is None:
        return jsonify({"erro": "Livro não encontrado"}), 404
    return jsonify(livro.to_dict())

@app.route("/livros", methods=["POST"])
def cadastrar_livro():
    dados = request.get_json()
    livro = Livro(
        titulo=dados["titulo"],
        autor=dados["autor"],
        ano=dados["ano"],
        genero=dados["genero"],
        paginas=dados["paginas"],
        editora=dados["editora"],
        edicao=dados["edicao"]
    )
    db.session.add(livro)
    db.session.commit()
    return jsonify(livro.to_dict()), 201

@app.route("/livros/<int:id>", methods=["PUT"])
def atualizar_livro(id):
    livro = Livro.query.get(id)
    if livro is None:
        return jsonify({"erro": "Livro não encontrado"}), 404
    dados = request.get_json()
    for chave, valor in dados.items():
        setattr(livro, chave, valor)
    db.session.commit()
    return jsonify(livro.to_dict())

@app.route("/livros/<int:id>", methods=["DELETE"])
def deletar_livro(id):
    livro = Livro.query.get(id)
    if livro is None:
        return jsonify({"erro": "Livro não encontrado"}), 404
    db.session.delete(livro)
    db.session.commit()
    return jsonify({"mensagem": "Livro removido com sucesso"})

if __name__ == "__main__":
    app.run(debug=True)