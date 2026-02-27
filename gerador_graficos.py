import matplotlib.pyplot as plt

def criar_grafico_barras():
    # Dados de exemplo: Meses e Vendas (ou qualquer outra métrica)
    categorias = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun']
    valores = [1500, 2300, 1800, 3200, 2800, 3500]
    
    # Criando a figura e definindo o tamanho
    plt.figure(figsize=(10, 6))
    
    # Gerando o gráfico de barras com uma cor moderna
    plt.bar(categorias, valores, color='#4C72B0')
    
    # Adicionando títulos e rótulos
    plt.title('Crescimento de Resultados no Semestre', fontsize=16)
    plt.xlabel('Período', fontsize=12)
    plt.ylabel('Volume', fontsize=12)
    
    # Adicionando uma grade sutil no fundo para facilitar a leitura
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Mostra o gráfico na tela (você pode salvar a imagem por lá)
    plt.tight_layout()
    plt.show()

# Basta chamar a função para a mágica acontecer
criar_grafico_barras()