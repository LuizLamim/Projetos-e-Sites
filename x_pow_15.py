import numpy as np
import matplotlib.pyplot as plt

# 1. Definindo o intervalo de x
# Geramos 400 pontos linearmente espaçados entre -1.5 e 1.5
x = np.linspace(-1.5, 1.5, 400)

# 2. Calculando a equação
y = x**15

# 3. Configurando a figura
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='$y = x^{15}$', color='blue', linewidth=2)