from app.livros.model import db, Livro

class LivroRepository:
    def listar_todos(self):
        return Livro.query.all()

    def buscar_por_id(self, id):
        return Livro.query.get(id)

    def salvar(self, livro):
        db.session.add(livro)
        db.session.commit()
        return livro

    def atualizar(self, livro, dados):
        for chave, valor in dados.items():
            setattr(livro, chave, valor)
        db.session.commit()
        return livro

    def deletar(self, livro):
        db.session.delete(livro)
        db.session.commit()