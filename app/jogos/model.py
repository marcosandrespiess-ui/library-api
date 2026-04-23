from app.extensions import db

jogo_plataforma = db.Table("jogo_plataforma",
    db.Column("jogo_id", db.Integer, db.ForeignKey("jogo.id")),
    db.Column("plataforma_id", db.Integer, db.ForeignKey("plataforma.id"))
    )

jogo_genero = db.Table("jogo_genero",
    db.Column("jogo_id", db.Integer, db.ForeignKey("jogo.id")),
    db.Column("genero_id", db.Integer, db.ForeignKey("genero.id"))
    )

jogo_modo = db.Table("jogo_modo",
    db.Column("jogo_id", db.Integer, db.ForeignKey("jogo.id")),
    db.Column("modo_id", db.Integer, db.ForeignKey("modo.id"))
)

class Plataforma(db.Model):
    id  = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False, unique=True)

class Genero(db.Model):
    id  = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False, unique=True)

class Modo(db.Model):
    id  = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False, unique=True)

class Jogo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    desenvolvedora = db.Column(db.String(200), nullable=False)
    subgenero = db.Column(db.String(100))
    capa_url = db.Column(db.String(500), nullable=True)

    plataformas = db.relationship("Plataforma", secondary=jogo_plataforma)
    generos = db.relationship("Genero", secondary=jogo_genero)
    modos = db.relationship("Modo", secondary=jogo_modo)

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "ano": self.ano,
            "desenvolvedora": self.desenvolvedora,
            "subgenero": self.subgenero,
            "capa_url": self.capa_url,
            "plataformas": [p.nome for p in self.plataformas],
            "generos": [g.nome for g in self.generos],
            "modos": [m.nome for m in self.modos]
        }