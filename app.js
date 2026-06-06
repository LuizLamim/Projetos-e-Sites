const express = require('express');
const app = express();
const PORT = 3000;

// Middleware para entender JSON no corpo da requisição
app.use(express.json());

// Rota GET: A página inicial
app.get('/', (req, res) => {
  res.send('<h1>Olá! Servidor Node.js rodando com sucesso.</h1>');
});

// Rota GET: Exemplo de uma API simples
app.get('/api/usuario', (req, res) => {
  res.json({
    id: 1,
    nome: 'Colaborador Gemini',
    cargo: 'IA Assistente'
  });
});

// Iniciar o servidor
app.listen(PORT, () => {
  console.log(`Servidor rodando em http://localhost:${PORT}`);
});