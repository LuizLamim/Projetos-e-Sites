import sqlite3

def gerenciar_banco():
    # 1. Cria a conexão com o banco de dados
    # Se o arquivo 'meu_banco.db' não existir, ele será criado automaticamente.
    conexao = sqlite3.connect('meu_banco.db')
    
    # 2. Cria o cursor (o objeto que executa os comandos SQL)
    cursor = conexao.cursor()

    try:
        # --- CRIAR TABELA ---
        print("Criando tabela...")
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER,
                email TEXT
            )
        ''')

        # --- INSERIR DADOS ---
        # Usamos '?' como placeholder para evitar SQL Injection (segurança)
        print("Inserindo dados...")
        dados_novos = [
            ('Ana Souza', 28, 'ana@email.com'),
            ('Carlos Silva', 35, 'carlos@email.com'),
            ('Beatriz Lima', 22, 'bia@email.com')
        ]
        
        cursor.executemany('''
            INSERT INTO usuarios (nome, idade, email) 
            VALUES (?, ?, ?)
        ''', dados_novos)

        # Salva as alterações no banco (commit)
        conexao.commit()

        # --- CONSULTAR DADOS (SELECT) ---
        print("\nLendo dados do banco:")
        cursor.execute("SELECT * FROM usuarios WHERE idade > 25")
        
        resultados = cursor.fetchall()
        
        for linha in resultados:
            print(f"ID: {linha[0]} | Nome: {linha[1]} | Idade: {linha[2]} | Email: {linha[3]}")

    except sqlite3.Error as erro:
        print(f"Erro ao interagir com o banco: {erro}")

    finally:
        # 3. Fecha a conexão para liberar recursos
        if conexao:
            conexao.close()
            print("\nConexão fechada.")

if __name__ == "__main__":
    gerenciar_banco()