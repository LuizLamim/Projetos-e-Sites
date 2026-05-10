import numpy as np
import matplotlib.pyplot as plt

# 1. Definir o intervalo de x (de 0 a 4pi para vermos dois ciclos completos)
# O linspace cria 400 pontos entre os valores para o gráfico ficar suave
x = np.linspace(0, 4 * np.pi, 400)

# 2. Calcular os valores de y
y = np.sin(x) + np.cos(x)

# 3. Criar a figura e o gráfico
plt.figure(figsize=(10, 6))
plt.plot(x, y, label=r'$f(x) = \sin(x) + \cos(x)$', color='blue', linewidth=2)