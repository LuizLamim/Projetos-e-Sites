import numpy as np
import matplotlib.pyplot as plt

# 1. Definir o intervalo de x (de -2π a 2π, com 1000 pontos para manter a curva suave)
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

# 2. Calcular os valores de y = |sen(x)|
# np.sin(x) calcula o seno, e np.abs() aplica o módulo (valor absoluto)
y = np.abs(np.sin(x))