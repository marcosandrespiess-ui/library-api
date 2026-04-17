from google import genai
import os
import json

def autocompletar_livro(titulo):
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    prompt = f"""
    Você é um assistente de biblioteca. O usuário digitou o título "{titulo}".
    
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
    
    Se não souber alguma informação, use valores padrão razoáveis.
    """

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )

    texto = response.text.strip()

    if texto.startswith("```"):
        texto = texto.split("```")[1]
        if texto.startswith("json"):
            texto = texto[4:]

    return json.loads(texto.strip())