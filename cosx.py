import numpy as np
import matplotlib.pyplot as plt

# 1. Definir o intervalo do eixo x (de -2π a 2π, com 1000 pontos para suavizar a curva)
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

# 2. Calcular o valor de y = |cos(x)|
y = np.abs(np.cos(x))

# 3. Criar e configurar o gráfico
plt.figure(figsize=(10, 5))
plt.plot(x, y, color='blue', linewidth=2, label=r'$y = |\cos(x)|$')

# 4. Formatar os eixos para mostrar valores em múltiplos de π
plt.xticks(
    [-2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi],
    [r'$-2\pi$', r'$-\pi$', '0', r'$\pi$', r'$2\pi$']
)

# 5. Adicionar títulos, rótulos e grade
plt.title("Gráfico da Função Valor Absoluto do Cosseno", fontsize=14)
plt.xlabel("Eixo x (radianos)", fontsize=12)
plt.ylabel("Eixo y", fontsize=12)
plt.axhline(0, color='black', linewidth=1) # Linha do eixo x
plt.axvline(0, color='black', linewidth=1) # Linha do eixo y
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)

# 6. Exibir o gráfico
plt.show()