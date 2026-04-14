from flask import Blueprint, jsonify, request
from app.services.livro_service import LivroService
from app.repositories.livro_repository import LivroRepository

livro_bp = Blueprint("livros", __name__)
service = LivroService(repository=LivroRepository())

@livro_bp.route("/livros", methods=["GET"])
def listar_livros():
    livros = service.listar_todos()
    return jsonify([l.to_dict() for l in livros])

@livro_bp.route("/livros/<int:id>", methods=["GET"])
def buscar_livro(id):
    livro = service.buscar_por_id(id)
    if livro is None:
        return jsonify({"erro": "Livro não encontrado"}), 404
    return jsonify(livro.to_dict())

@livro_bp.route("/livros", methods=["POST"])
def cadastrar_livro():
    dados = request.get_json()
    livro = service.cadastrar(dados)
    return jsonify(livro.to_dict()), 201

@livro_bp.route("/livros/<int:id>", methods=["PUT"])
def atualizar_livro(id):
    dados = request.get_json()
    livro = service.atualizar(id, dados)
    if livro is None:
        return jsonify({"erro": "Livro não encontrado"}), 404
    return jsonify(livro.to_dict())

@livro_bp.route("/livros/<int:id>", methods=["DELETE"])
def deletar_livro(id):
    sucesso = service.deletar(id)
    if not sucesso:
        return jsonify({"erro": "Livro não encontrado"}), 404
    return jsonify({"mensagem": "Livro removido com sucesso"})