import requests
from bs4 import BeautifulSoup

def verificar_preco(url, preco_alvo):
    # Um "disfarce" para o site achar que somos um navegador real e não um robô
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        # Acessa a página
        resposta = requests.get(url, headers=headers)
        sopa = BeautifulSoup(resposta.text, 'html.parser')
        
        # OBS: A classe 'price' varia de site para site. 
        # Este é um exemplo genérico. Inspecione a página para achar a classe correta!
        elemento_preco = sopa.find(class_="price") # Substitua pela classe do site alvo
        
        if elemento_preco:
            # Pega o texto, tira o 'R$' e converte para número
            preco_texto = elemento_preco.get_text().replace('R$', '').replace('.', '').replace(',', '.').strip()
            preco_atual = float(preco_texto)
            
            print(f"Preço atual: R$ {preco_atual:.2f}")
            
            if preco_atual <= preco_alvo:
                print("🚨 ALERTA: O preço caiu! Hora de comprar!")
            else:
                print("Ainda está caro. Continue esperando.")
        else:
            print("Não foi possível encontrar o preço na página.")
            
    except Exception as e:
        print(f"Erro ao acessar o site: {e}")

# Como usar:
link_do_produto = "https://www.exemplo.com.br/produto"
meu_orcamento = 1500.00

verificar_preco(link_do_produto, meu_orcamento)