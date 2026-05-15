import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def realizar_mineracao_dados():
    # 1. Criação de um conjunto de dados simulado (Cliques vs. Conversões)
    np.random.seed(42)
    dados = {
        'Cliques': np.random.randint(100, 2000, 100),
        'Conversoes': np.random.randint(5, 200, 100)
    }
    df = pd.DataFrame(dados)
    
    print("Visualização dos 5 primeiros registros:")
    print(df.head(), "\n")

    # 2. Pré-processamento: Padronização dos dados
    # É crucial em mineração de dados colocar as variáveis na mesma escala
    scaler = StandardScaler()
    dados_escalados = scaler.fit_transform(df)

    # 3. Aplicação do Algoritmo K-Means
    # Vamos pedir para o algoritmo encontrar 3 grupos distintos (clusters)
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    df['Grupo'] = kmeans.fit_predict(dados_escalados)

    # 4. Análise dos Resultados
    print("Média de Cliques e Conversões por Grupo:")
    print(df.groupby('Grupo').mean(), "\n")

    # 5. Visualização dos Clusters
    plt.figure(figsize=(8, 6))
    cores = ['red', 'green', 'blue']