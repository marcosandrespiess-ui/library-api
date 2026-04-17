const API_URL = "http://127.0.0.1:5000";

async function listarLivros() {
    const response = await fetch(`${API_URL}/livros`);
    return await response.json();
}

async function buscarLivro(id) {
    const response = await fetch(`${API_URL}/livros/${id}`);
    return await response.json();
}

async function cadastrarLivro(dados) {
    const response = await fetch(`${API_URL}/livros`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(dados)
    });
    return await response.json();
}

async function atualizarLivro(id, dados) {
    const response = await fetch(`${API_URL}/livros/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(dados)
    });
    return await response.json();
}

async function deletarLivro(id) {
    const response = await fetch(`${API_URL}/livros/${id}`, {
        method: "DELETE"
    });
    return await response.json();
}