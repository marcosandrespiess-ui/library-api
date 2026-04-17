from app.livros.service import LivroService

class RepositorioFalso:
    def __init__(self):
        self.livros = []
        self.proximo_id = 1

    def listar_todos(self):
        return self.livros

    def buscar_por_id(self, id):
        return next((l for l in self.livros if l.id == id), None)

    def salvar(self, livro):
        livro.id = self.proximo_id
        self.proximo_id += 1
        self.livros.append(livro)
        return livro

    def atualizar(self, livro, dados):
        for chave, valor in dados.items():
            setattr(livro, chave, valor)
        return livro

    def deletar(self, livro):
        self.livros.remove(livro)


def fazer_service():
    return LivroService(repository=RepositorioFalso())


def dados_livro():
    return {
        "titulo": "O Senhor dos Anéis",
        "autor": "J.R.R. Tolkien",
        "ano": 1954,
        "genero": "Fantasia",
        "paginas": 1200,
        "editora": "Allen & Unwin",
        "edicao": 1
    }


def test_cadastrar_livro():
    service = fazer_service()
    livro = service.cadastrar(dados_livro())
    assert livro.titulo == "O Senhor dos Anéis"
    assert livro.autor == "J.R.R. Tolkien"
    assert livro.id == 1


def test_listar_livros():
    service = fazer_service()
    service.cadastrar(dados_livro())
    service.cadastrar(dados_livro())
    livros = service.listar_todos()
    assert len(livros) == 2


def test_buscar_livro_existente():
    service = fazer_service()
    service.cadastrar(dados_livro())
    livro = service.buscar_por_id(1)
    assert livro is not None
    assert livro.titulo == "O Senhor dos Anéis"


def test_buscar_livro_inexistente():
    service = fazer_service()
    livro = service.buscar_por_id(99)
    assert livro is None


def test_atualizar_livro():
    service = fazer_service()
    service.cadastrar(dados_livro())
    livro = service.atualizar(1, {"ano": 1955})
    assert livro.ano == 1955


def test_deletar_livro():
    service = fazer_service()
    service.cadastrar(dados_livro())
    sucesso = service.deletar(1)
    assert sucesso == True
    assert service.buscar_por_id(1) is None


def test_deletar_livro_inexistente():
    service = fazer_service()
    sucesso = service.deletar(99)
    assert sucesso == False