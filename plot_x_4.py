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