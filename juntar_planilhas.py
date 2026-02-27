import pandas as pd
import os
import glob

def consolidar_csvs(caminho_pasta, arquivo_saida):
    # Encontra todos os arquivos .csv na pasta informada
    padrao_busca = os.path.join(caminho_pasta, "*.csv")
    lista_arquivos = glob.glob(padrao_busca)
    
    if not lista_arquivos:
        print("Nenhum arquivo CSV encontrado nesta pasta.")
        return
        
    print(f"Encontrados {len(lista_arquivos)} arquivos. Consolidando...")
    
    # Lê cada arquivo e junta em uma lista
    lista_dataframes = []
    for arquivo in lista_arquivos:
        # Lendo o CSV. Se der erro de acentuação, mude o encoding para 'latin1'
        df = pd.read_csv(arquivo, encoding='utf-8')
        lista_dataframes.append(df)
        
    # Combina todos os DataFrames de uma vez
    tabela_consolidada = pd.concat(lista_dataframes, ignore_index=True)
    
    # Salva o resultado final em um novo arquivo
    caminho_saida = os.path.join(caminho_pasta, arquivo_saida)
    tabela_consolidada.to_csv(caminho_saida, index=False, encoding='utf-8')
    
    print(f"Sucesso! Arquivo salvo como: {arquivo_saida}")

# Como usar:
pasta_dos_relatorios = r"C:\Users\SeuUsuario\Documentos\Relatorios"
consolidar_csvs(pasta_dos_relatorios, "relatorio_anual_consolidado.csv")