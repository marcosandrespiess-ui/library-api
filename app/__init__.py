from flask import Flask
from app.models.livro import db
from app.routes.livro_routes import livro_bp

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///livros.db"
    
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
    
    app.register_blueprint(livro_bp)
    
    return app