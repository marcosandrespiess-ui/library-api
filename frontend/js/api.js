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

async function listarJogos() {
    const response = await fetch(`${API_URL}/jogos`);
    return await response.json();
}

async function buscarJogo(id) {
    const response = await fetch(`${API_URL}/jogos/${id}`);
    return await response.json();
}

async function cadastrarJogo(dados) {
    const response = await fetch(`${API_URL}/jogos`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(dados)
    });
    return await response.json();
}

async function atualizarJogo(id, dados) {
    const response = await fetch(`${API_URL}/jogos/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(dados)
    });
    return await response.json();
}

async function deletarJogo(id) {
    const response = await fetch(`${API_URL}/jogos/${id}`, {
        method: "DELETE"
    });
    return await response.json();
}