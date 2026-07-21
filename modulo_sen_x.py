import numpy as np
import matplotlib.pyplot as plt

# 1. Definir o intervalo de x (de -2π a 2π, com 1000 pontos para manter a curva suave)
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

# 2. Calcular os valores de y = |sen(x)|
# np.sin(x) calcula o seno, e np.abs() aplica o módulo (valor absoluto)
y = np.abs(np.sin(x))

# 3. Criar e configurar o gráfico
plt.figure(figsize=(10, 5))  # Define o tamanho da janela
plt.plot(x, y, label=r'$f(x) = |\sin(x)|$', color='blue', linewidth=2)

# 4. Adicionar detalhes visuais para facilitar a leitura
plt.title('Gráfico da função f(x) = |sen(x)|', fontsize=14, pad=15)
plt.xlabel('x (radianos)', fontsize=12)
plt.ylabel('f(x)', fontsize=12)

# Destacar os eixos X e Y
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

# Adicionar uma grade de fundo e a legenda
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)

# 5. Exibir o gráfico na tela
plt.show()