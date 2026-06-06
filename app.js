const express = require('express');
const app = express();
const PORT = 3000;

// Middleware para entender JSON no corpo da requisição
app.use(express.json());