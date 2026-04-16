from flask import jsonify

def registrar_erros(app):

    @app.errorhandler(400)
    def bad_request(e):
        return jsonify({"erro": "Requisição invalida", "status": 400}), 400
    
    @app.errorhandler(404)
    def not_found(e):
        return jsonify({"erro": "Recurso não encontrado", "status": 404}), 404  
    
    @app.errorhandler(405)
    def method_not_allowed(e):
        return jsonify({"erro": "Método não permitido", "status": 405}), 405   

    @app.errorhandler(500)  
    def internal_server_error(e):
        return jsonify({"erro": "Erro interno do servidor", "status": 500}), 500
     