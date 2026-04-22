from app.jogos.service import JogoService

class RepositorioFalso:
    def __init__(self):
        self.jogos = []
        self.proximo_id = 1

    def listar_todos(self):
        return self.jogos   
    
    def buscar_por_id(self, id):
        return next((j for j in self.jogos if j.id == id), None)
    
    def salvar(self, jogo, dados):
        jogo.plataformas = dados.get("plataformas", [])
        jogo.generos = dados.get("generos", [])
        jogo.modos = dados.get("modos", [])
        jogo.id = self.proximo_id
        self.proximo_id += 1
        self.jogos.append(jogo)
        return jogo
    
    def atualizar(self, jogo, dados):
        for chave in ["nome", "ano", "desenvolvedora", "subgenero"]:
            if chave in dados:
                setattr(jogo, chave, dados[chave])
        if "plataformas" in dados:
            jogo.plataformas = dados["plataformas"]
        if "generos" in dados:
            jogo.generos = dados["generos"]
        if "modos" in dados:
            jogo.modos = dados["modos"]
        return jogo 
    
    def deletar(self, jogo):
        self.jogos.remove(jogo)


def fazer_service():
    return JogoService(repository=RepositorioFalso())

def dados_jogo():
    return {
        "nome": "The Legend of Zelda",
        "ano": 1986,
        "desenvolvedora": "Nintendo",
        "subgenero": "Aventura",
        "plataformas": ["NES"],
        "generos": ["Aventura", "RPG"],
        "modos": ["Single-player"]
    }
    
def test_cadastrar_jogo():
    service = fazer_service()
    jogo = service.cadastrar(dados_jogo())
    assert jogo.nome == "The Legend of Zelda"
    assert jogo.desenvolvedora == "Nintendo"
    assert jogo.id == 1

def test_listar_jogos():
    service = fazer_service()
    service.cadastrar(dados_jogo())
    service.cadastrar(dados_jogo())
    jogos = service.listar_todos()
    assert len(jogos) == 2

def test_buscar_jogo_existente():
    service = fazer_service()
    service.cadastrar(dados_jogo())
    jogo = service.buscar_por_id(1)
    assert jogo is not None
    assert jogo.nome == "The Legend of Zelda"

def test_buscar_jogo_inexistente():
    service = fazer_service()
    jogo = service.buscar_por_id(99)
    assert jogo is None

def test_atualizar_jogo():
    service = fazer_service()
    jogo = service.cadastrar(dados_jogo())
    dados_atualizados = {
        "nome": "The Legend of Zelda: Updated",
        "ano": 1987,
        "desenvolvedora": "Nintendo EAD",
        "subgenero": "Ação-Aventura",
        "plataformas": ["NES", "SNES"],
        "generos": ["Ação", "Aventura"],
        "modos": ["Single-player", "Multiplayer"]
    }
    jogo_atualizado = service.atualizar(jogo.id, dados_atualizados)
    assert jogo_atualizado.nome == "The Legend of Zelda: Updated"
    assert jogo_atualizado.ano == 1987
    assert jogo_atualizado.desenvolvedora == "Nintendo EAD"
    assert jogo_atualizado.subgenero == "Ação-Aventura"
    assert jogo_atualizado.plataformas == ["NES", "SNES"]
    assert jogo_atualizado.generos == ["Ação", "Aventura"]
    assert jogo_atualizado.modos == ["Single-player", "Multiplayer"]    

def test_deletar_jogo():
    service = fazer_service()
    jogo = service.cadastrar(dados_jogo())
    sucesso = service.deletar(jogo.id)
    assert sucesso == True
    assert service.buscar_por_id(jogo.id) is None   

def test_deletar_jogo_inexistente():
    service = fazer_service()
    sucesso = service.deletar(99)
    assert sucesso == False 

