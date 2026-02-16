import sqlite3

def gerenciar_banco():
    # 1. Cria a conexão com o banco de dados
    # Se o arquivo 'meu_banco.db' não existir, ele será criado automaticamente.
    conexao = sqlite3.connect('meu_banco.db')
    
    # 2. Cria o cursor (o objeto que executa os comandos SQL)
    cursor = conexao.cursor()