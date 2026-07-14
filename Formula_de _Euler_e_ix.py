import numpy as np
import matplotlib.pyplot as plt

# 1. Definir o intervalo de x (de 0 a 4*pi para mostrar dois ciclos completos)
x = np.linspace(0, 4 * np.pi, 500)

# 2. Calcular a função e^(ix)
# Em Python, 'j' é usado para representar a unidade imaginária (i)
y = np.exp(1j * x)

# 3. Separar as partes real e imaginária
parte_real = np.real(y)  # Equivalente a cos(x)
parte_imag = np.imag(y)  # Equivalente a sin(x)

# 4. Configurar e plotar o gráfico
plt.figure(figsize=(10, 5))