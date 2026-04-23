from app.extensions import db

class Livro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    autor = db.Column(db.String(200), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    genero = db.Column(db.String(100), nullable=False)
    paginas = db.Column(db.Integer, nullable=False)
    editora = db.Column(db.String(200), nullable=False)
    edicao = db.Column(db.Integer, nullable=False)
    capa_url = db.Column(db.String(500), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "autor": self.autor,
            "ano": self.ano,
            "genero": self.genero,
            "paginas": self.paginas,
            "editora": self.editora,
            "edicao": self.edicao,
            "capa_url": self.capa_url
        }