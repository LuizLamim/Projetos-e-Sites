import matplotlib.pyplot as plt
import numpy as np

# Definindo o número de lados do hectágono
lados = 100

# Calculando os ângulos para cada um dos 100 vértices (de 0 a 2*pi)
# Adicionamos um ponto extra no final para fechar o polígono perfeitamente
angulos = np.linspace(0, 2 * np.pi, lados + 1)

# Calculando as coordenadas X e Y usando o círculo unitário (raio = 1)
x = np.cos(angulos)
y = np.sin(angulos)

# Criando a figura
plt.figure(figsize=(6, 6))