from flask import Blueprint, jsonify, request
from app.ia.service import autocompletar_livro

ia_bp = Blueprint("ia", __name__)

@ia_bp.route("/livros/autocompletar", methods=["POST"])
def autocompletar():
    dados = request.get_json()
    titulo = dados.get("titulo", "")

    if not titulo:
        return jsonify({"erro": "Título é obrigatório"}), 400

    try:
        livro = autocompletar_livro(titulo)
        return jsonify(livro)
    except Exception as e:
        return jsonify({"erro": str(e)}), 500