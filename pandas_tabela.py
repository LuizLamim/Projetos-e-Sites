import pandas as pd

def organizar_planilha(caminho_entrada, caminho_saida, coluna_ordenacao):
    try:
        # 1. Carregar a tabela
        df = pd.read_excel(caminho_entrada)
        
        # 2. Remover duplicatas (baseado em todas as colunas)
        df = df.drop_duplicates()
        
        # 3. Ordenar por uma coluna específica
        if coluna_ordenacao in df.columns:
            df = df.sort_values(by=coluna_ordenacao)
        else:
            print(f"Aviso: Coluna '{coluna_ordenacao}' não encontrada.")

        # 4. Salvar o resultado
        df.to_excel(caminho_saida, index=False)
        print(f"Sucesso! Arquivo organizado salvo em: {caminho_saida}")