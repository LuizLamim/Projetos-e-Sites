import pandas as pd

def converter_json_para_csv(arquivo_json, arquivo_destino):
    try:
        # O Pandas lê a estrutura JSON e já a transforma em uma tabela
        dados = pd.read_json(arquivo_json)
        
        # Exporta para CSV (que pode ser aberto no Excel ou Google Sheets)
        dados.to_csv(arquivo_destino, index=False, encoding='utf-8')
        print(f"Conversão concluída! Tabela salva em: {arquivo_destino}")
        
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Como usar:
arquivo_origem = "dados_do_sistema.json"
arquivo_final = "planilha_limpa.csv"

converter_json_para_csv(arquivo_origem, arquivo_final)