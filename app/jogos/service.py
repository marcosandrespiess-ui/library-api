from app.jogos.model import Jogo, Plataforma, Genero, Modo
from app.jogos.repository import JogoRepository

class JogoService:
    def __init__(self, repository=None):
        self.repository = repository or JogoRepository()

    def listar_todos(self):
        return self.repository.listar_todos()
    
    def buscar_por_id(self, id):
        return self.repository.buscar_por_id(id)    
    
    def cadastrar(self, dados):
        jogo = Jogo(
            nome=dados["nome"],
            desenvolvedora=dados["desenvolvedora"],
            ano=dados["ano"],
            subgenero=dados.get("subgenero")
        )
        return self.repository.salvar(jogo, dados)
    
    def atualizar(self, id, dados):
        jogo = self.repository.buscar_por_id(id)
        if jogo is None:
            return None
        return self.repository.atualizar(jogo, dados)       
    
    def deletar(self, id):
        jogo = self.repository.buscar_por_id(id)
        if jogo is None:
            return False
        self.repository.deletar(jogo)
        return True
    
