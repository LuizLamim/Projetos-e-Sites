-- 1. Criar o banco de dados
CREATE DATABASE SistemaBusca;
USE SistemaBusca;

-- 2. Criar a tabela de usuários/pessoas
CREATE TABLE Pessoas (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome_completo VARCHAR(255) NOT NULL,
    email VARCHAR(100),
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);