from app.jogos.model import Plataforma, Genero, Modo, Jogo  
from app.extensions import db

class JogoRepository:
    def listar_todos(self):
        return Jogo.query.all()

    def buscar_por_id(self, id):
        return Jogo.query.get(id)

    def salvar(self, jogo, dados):
        jogo.plataformas = [Plataforma.query.filter_by(nome=nome).first() or Plataforma(nome=nome) for nome in dados.get("plataformas", [])]
        jogo.generos = [Genero.query.filter_by(nome=nome).first() or Genero(nome=nome) for nome in dados.get("generos", [])]
        jogo.modos = [Modo.query.filter_by(nome=nome).first() or Modo(nome=nome) for nome in dados.get("modos", [])]

        db.session.add(jogo)
        db.session.commit()
        return jogo

    def atualizar(self, dados, jogo):
        for chave, valor in dados.get("plataformas", {}).items():
            setattr(jogo, chave, valor)
        for chave, valor in dados.get("generos", {}).items():
            setattr(jogo, chave, valor)
        for chave, valor in dados.get("modos", {}).items():
            setattr(jogo, chave, valor)
        db.session.commit()
        return jogo


    def deletar(self, jogo):
        db.session.delete(jogo)
        db.session.commit()