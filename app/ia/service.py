import anthropic
import os
import json

def autocompletar_livro(titulo):
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    prompt = f"""O usuário digitou o título "{titulo}".
    
Retorne APENAS um JSON válido com as informações do livro, sem nenhum texto adicional, sem markdown, sem explicações.

Formato exato:
{{
    "titulo": "título completo e correto",
    "autor": "nome do autor",
    "ano": ano de publicação como número inteiro,
    "genero": "um dos seguintes: Fantasia, Ficcao, Terror, Romance, Aventura, Misterio, Historia, Biografia, Ciencia, Outro",
    "paginas": número de páginas como inteiro,
    "editora": "nome da editora original",
    "edicao": 1
}}

Se não souber alguma informação, use valores padrão razoáveis."""

    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    texto = message.content[0].text.strip()

    if texto.startswith("```"):
        texto = texto.split("```")[1]
        if texto.startswith("json"):
            texto = texto[4:]

    return json.loads(texto.strip())


def autocompletar_jogo(nome):
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    prompt = f"""O usuário digitou o nome do jogo "{nome}".
    
Retorne APENAS um JSON válido com as informações do jogo, sem nenhum texto adicional, sem markdown, sem explicações.

Formato exato:
{{
    "nome": "nome completo e correto do jogo",
    "ano": ano de lançamento como número inteiro,
    "desenvolvedora": "nome da desenvolvedora",
    "subgenero": "subgênero do jogo ou null",
    "plataformas": ["lista", "de", "plataformas"],
    "generos": ["lista", "de", "generos"],
    "modos": ["Single-player", "Multiplayer"],
    "capa_url": "URL direta de uma imagem da capa do jogo no wikipedia ou igdb ou similar"
}}

Se não souber alguma informação, use valores padrão razoáveis."""

    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )

    texto = message.content[0].text.strip()
    if texto.startswith("```"):
        texto = texto.split("```")[1]
        if texto.startswith("json"):
            texto = texto[4:]

    return json.loads(texto.strip())