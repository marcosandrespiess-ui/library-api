from flask import Flask
from app.models.livro import db
from app.routes.livro_routes import livro_bp
from app.errors import registrar_erros

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///livros.db"
    app.config["PROPAGATE_EXCEPTIONS"] = False  
    
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
    
    app.register_blueprint(livro_bp)
    registrar_erros(app)
    
    return app