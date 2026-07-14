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

# Plotando as duas curvas
plt.plot(x, parte_real, label='Parte Real (cos(x))', color='#1f77b4', linewidth=2)
plt.plot(x, parte_imag, label='Parte Imaginária (sin(x))', color='#ff7f0e', linestyle='--', linewidth=2)

# Adicionando detalhes ao gráfico
plt.title('Gráfico da Fórmula de Euler: e^(ix) = cos(x) + i*sin(x)', fontsize=14)
plt.xlabel('x (radianos)', fontsize=12)
plt.ylabel('Amplitude', fontsize=12)

# Linha do eixo X e grade
plt.axhline(0, color='black', linewidth=1)
plt.grid(True, linestyle=':', alpha=0.7)

# Adicionando a legenda
plt.legend(loc='upper right', fontsize=11)

# Exibir o gráfico
plt.tight_layout()
plt.show()