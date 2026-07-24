import numpy as np
import matplotlib.pyplot as plt

# 1. Definir o intervalo do eixo x (de -2π a 2π, com 1000 pontos para suavizar a curva)
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

# 2. Calcular o valor de y = |cos(x)|
y = np.abs(np.cos(x))

# 3. Criar e configurar o gráfico
plt.figure(figsize=(10, 5))
plt.plot(x, y, color='blue', linewidth=2, label=r'$y = |\cos(x)|$')