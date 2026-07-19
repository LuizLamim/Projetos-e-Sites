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

# Plotando as linhas do hectágono e destacando os vértices em vermelho
plt.plot(x, y, color="blue", linewidth=1.5, label="Lados (100)")
plt.scatter(
    x[:-1], y[:-1], color="red", s=10, zorder=3, label="Vértices (100)"
)

# Ajustes estéticos para o gráfico ficar bonito e centralizado
plt.title("Gráfico de um Hectágono Regular", fontsize=14, fontweight="bold")
plt.axis("equal")  # Garante que o polígono não fique achatado (proporção 1:1)
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend(loc="upper right")

# Exibindo o gráfico
plt.show()