import numpy as np
import matplotlib.pyplot as plt

# 1. Definir o intervalo de x (de -2π a 2π com 1000 pontos para suavidade)
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)


# 2. Calcular a cotangente (1 / tangente)
# Usamos um pequeno aviso de ignorar divisão por zero para evitar poluir o terminal
with np.errstate(divide='ignore'):
    y = 1 / np.tan(x)