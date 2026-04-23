from flask import Blueprint, jsonify, request
from app.ia.service import autocompletar_livro, autocompletar_jogo

ia_bp = Blueprint("ia", __name__)

@ia_bp.route("/livros/autocompletar", methods=["POST"])
def autocompletar_livro_route():
    dados = request.get_json()
    titulo = dados.get("titulo", "")

    if not titulo:
        return jsonify({"erro": "Título é obrigatório"}), 400

    try:
        livro = autocompletar_livro(titulo)
        return jsonify(livro)
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@ia_bp.route("/jogos/autocompletar", methods=["POST"])
def autocompletar_jogo_route():
    dados = request.get_json()
    nome = dados.get("nome", "")

    if not nome:
        return jsonify({"erro": "Nome é obrigatório"}), 400

    try:
        jogo = autocompletar_jogo(nome)
        return jsonify(jogo)
    except Exception as e:
        return jsonify({"erro": str(e)}), 500