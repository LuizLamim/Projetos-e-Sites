CREATE DATABASE MinhaLoja;
USE MinhaLoja;

-- Tabela de Clientes
CREATE TABLE Clientes (
    ClienteID INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    DataCadastro DATE NOT NULL
);

-- Tabela de Produtos
CREATE TABLE Produtos (
    ProdutoID INT AUTO_INCREMENT PRIMARY KEY,
    NomeProduto VARCHAR(100) NOT NULL,
    Preco DECIMAL(10, 2) NOT NULL,
    Estoque INT NOT NULL
);

-- Tabela de Pedidos (Relaciona Clientes e Produtos)
CREATE TABLE Pedidos (
    PedidoID INT AUTO_INCREMENT PRIMARY KEY,
    ClienteID INT,
    ProdutoID INT,
    Quantidade INT NOT NULL,
    DataPedido TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ClienteID) REFERENCES Clientes(ClienteID),
    FOREIGN KEY (ProdutoID) REFERENCES Produtos(ProdutoID)
);

-- Inserindo Clientes
INSERT INTO Clientes (Nome, Email, DataCadastro) VALUES
('Ana Silva', 'ana.silva@email.com', '2023-10-01'),
('Carlos Souza', 'carlos.souza@email.com', '2023-10-05'),
('Beatriz Lima', 'beatriz.lima@email.com', '2023-10-10');

-- Inserindo Produtos
INSERT INTO Produtos (NomeProduto, Preco, Estoque) VALUES
('Notebook', 3500.00, 15),
('Mouse Sem Fio', 120.50, 50),
('Teclado Mecânico', 450.00, 30);

-- Inserindo Pedidos (Simulando compras)
INSERT INTO Pedidos (ClienteID, ProdutoID, Quantidade) VALUES
(1, 1, 1), -- Ana comprou 1 Notebook
(1, 2, 2), -- Ana comprou 2 Mouses
(2, 3, 1), -- Carlos comprou 1 Teclado
(3, 1, 1); -- Beatriz comprou 1 Notebook

SELECT 
    c.Nome AS Cliente,
    p.NomeProduto AS Produto,
    pd.Quantidade,
    p.Preco AS PrecoUnitario,
    (pd.Quantidade * p.Preco) AS ValorTotalProduto,
    pd.DataPedido
