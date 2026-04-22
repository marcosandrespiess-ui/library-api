from flask import Flask
from flask_cors import CORS
from app.extensions import db
from app.livros.routes import livro_bp
from app.jogos.routes import jogos_bp
from app.ia.routes import ia_bp
from app.errors import registrar_erros
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///livros.db")
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "chave-padrao")
    app.config["PROPAGATE_EXCEPTIONS"] = False

    CORS(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(livro_bp)
    app.register_blueprint(jogos_bp)
    app.register_blueprint(ia_bp)
    registrar_erros(app)

    return app