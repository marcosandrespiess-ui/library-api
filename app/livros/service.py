from app.livros.model import Livro
from app.livros.repository import LivroRepository

class LivroService:
    def __init__(self, repository=None):
        self.repository = repository or LivroRepository()

    def listar_todos(self):
        return self.repository.listar_todos()

    def buscar_por_id(self, id):
        return self.repository.buscar_por_id(id)

    def cadastrar(self, dados):
        livro = Livro(
            titulo=dados["titulo"],
            autor=dados["autor"],
            ano=dados["ano"],
            genero=dados["genero"],
            paginas=dados["paginas"],
            editora=dados["editora"],
            edicao=dados["edicao"]
        )
        return self.repository.salvar(livro)

    def atualizar(self, id, dados):
        livro = self.repository.buscar_por_id(id)
        if livro is None:
            return None
        return self.repository.atualizar(livro, dados)

    def deletar(self, id):
        livro = self.repository.buscar_por_id(id)
        if livro is None:
            return False
        self.repository.deletar(livro)
        return True