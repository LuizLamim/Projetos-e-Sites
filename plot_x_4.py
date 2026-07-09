import matplotlib.pyplot as plt
import numpy as np

# 1. Definir o intervalo de valores para o eixo X
# np.linspace cria 400 pontos distribuídos uniformemente entre -5 e 5
x = np.linspace(-5, 5, 400)

# 2. Calcular os valores do eixo Y (a função x^4)
y = x**4

# 3. Configurar a figura do gráfico
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='$y = x^4$', color='blue', linewidth=2)

# 4. Adicionar detalhes visuais (título, rótulos e grade)
plt.title('Gráfico da Função $y = x^4$', fontsize=14)
plt.xlabel('Eixo X', fontsize=12)
plt.ylabel('Eixo Y', fontsize=12)

# Adiciona uma linha de grade para facilitar a leitura
plt.grid(True, linestyle='--', alpha=0.7)

# Adiciona a legenda
plt.legend(fontsize=12)

# 5. Exibir o gráfico na tela
plt.show()