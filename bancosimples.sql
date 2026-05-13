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

-- 3. Inserir dados para teste
INSERT INTO Pessoas (nome_completo, email) VALUES 
('Ana Maria Silva', 'ana.silva@email.com'),
('João Pedro Santos', 'joao.ps@email.com'),
('Mariana Oliveira', 'mari.oli@email.com'),
('Carlos Andrade Silva', 'carlos.a@email.com'),
('Beatriz Souza', 'bea.souza@email.com');

-- Criar um índice no campo nome para acelerar as buscas
--CREATE INDEX idx_nome ON Pessoas(nome_completo);

--Útil para encontrar um registro específico.
--SELECT * FROM Pessoas WHERE nome_completo = 'Ana Maria Silva';

-- Busca nomes que começam com "Mar"
--SELECT * FROM Pessoas WHERE nome_completo LIKE 'Mar%';
