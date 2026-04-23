import requests
import urllib3
urllib3.disable_warnings()

HEADERS = {"User-Agent": "library-api/1.0 (educational project)"}

def buscar_capa_livro(titulo, autor=None):
    try:
        query = titulo
        if autor:
            query += f" {autor}"
        
        url = f"https://openlibrary.org/search.json?q={query}&limit=1"
        response = requests.get(url, timeout=5, verify=False, headers=HEADERS)
        data = response.json()

        if data["docs"]:
            doc = data["docs"][0]
            if "cover_i" in doc:
                cover_id = doc["cover_i"]
                return f"https://covers.openlibrary.org/b/id/{cover_id}-L.jpg"
    except Exception:
        pass
    return None


def buscar_capa_jogo(nome):
    print(f"Buscando capa para: {nome}")
    try:
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{nome.replace(' ', '_')}"
        print(f"URL: {url}")
        response = requests.get(url, timeout=5, verify=False, headers=HEADERS)
        print(f"Status: {response.status_code}")
        data = response.json()
        print(f"Thumbnail: {data.get('thumbnail', 'SEM THUMBNAIL')}")
        if "thumbnail" in data:
            return data["thumbnail"]["source"]
    except Exception as e:
        print(f"Erro: {e}")
    return None