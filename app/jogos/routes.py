from flask import Blueprint, jsonify, request
from app.jogos.service import JogoService
from app.jogos.repository import JogoRepository
from app.jogos.schema import JogoSchema
from pydantic import ValidationError

jogos_bp = Blueprint("jogos", __name__)
service = JogoService(repository=JogoRepository())

@jogos_bp.route("/jogos", methods=["GET"])
def listar_jogos():
    jogos = service.listar_todos()
    return jsonify([j.to_dict() for j in jogos])

@jogos_bp.route("/jogos/<int:id>", methods=["GET"])
def buscar_jogo(id: int):
    jogo = service.buscar_por_id(id)
    if not jogo:
        return jsonify({"erro": "Jogo não encontrado"}), 404
    return jsonify(jogo.to_dict())

@jogos_bp.route("/jogos", methods=["POST"]) 
def cadastrar_jogo():
    try:
        dados = JogoSchema(**request.get_json())
    except ValidationError as e:
        return jsonify({"erro": e.errors()}), 400
    jogo = service.cadastrar(dados.model_dump())
    return jsonify(jogo.to_dict()), 201

@jogos_bp.route("/jogos/<int:id>", methods=["PUT"])
def atualizar_jogo(id: int):    
    try:
        dados = JogoSchema(**request.get_json())
    except ValidationError as e:
        return jsonify({"erro": e.errors()}), 400
    jogo = service.atualizar(id, dados.model_dump())
    if not jogo:
        return jsonify({"erro": "Jogo não encontrado"}), 404
    return jsonify(jogo.to_dict())

@jogos_bp.route("/jogos/<int:id>", methods=["DELETE"])
def deletar_jogo(id: int):      
    sucesso = service.deletar(id)
    if not sucesso:
        return jsonify({"erro": "Jogo não encontrado"}), 404
    return jsonify({"message": "Jogo removido com sucesso"})