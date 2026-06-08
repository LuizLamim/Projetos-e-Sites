// Usando a API pública JSONPlaceholder para demonstrar a conexão
const API_URL = 'https://jsonplaceholder.typicode.com/posts/1';

async function buscarDadosDaApi(){
    try {
        console.log('Tentando conectar à API...');

        // Realizando a requisição GET
        const resposta = await fetch(API_URL);

        // Verificando se a resposta foi bem-sucedida
        if (!resposta.ok) {
            throw new Error(`Erro na conexão: ${resposta.status}`);
        }

        // Convertendo o resultado para JSON
        const dados = await resposta.json();

        console.log('--- Dados recebidos com sucesso! ---');
        console.log(dados);
        
    } catch (erro) {
        console.error('Ocorreu um erro ao buscar os dados:', erro.message);
    }
}

// Chamada da função
buscarDadosDaApi();