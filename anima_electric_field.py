import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- Configurações Iniciais da Simulação ---
# Constante eletrostática (normalizada para 1 para simplificar a escala)
K = 1.0  

# Configuração do espaço (Grade de pontos onde o campo será calculado)
X, Y = np.meshgrid(np.linspace(-5, 5, 20), np.linspace(-5, 5, 20))

# Função para calcular o campo elétrico gerado por uma carga em um ponto
def calcular_campo_carga(q, pos_carga, X, Y):
    # Vetores de distância da carga até cada ponto da grade
    Rx = X - pos_carga[0]
    Ry = Y - pos_carga[1]
    R2 = Rx**2 + Ry**2
    R = np.sqrt(R2)
    
    # Evita divisão por zero no centro da carga
    R2[R2 == 0] = 1e-6
    R[R == 0] = 1e-3
    
    # Magnitude do campo E = K * q / r^2
    # Direção dada pelos vetores unitários (Rx/R, Ry/R)
    Ex = K * q * Rx / (R * R2)
    Ey = K * q * Ry / (R * R2)
    
    return Ex, Ey

# --- Configuração do Gráfico ---
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')
ax.set_title("Simulação Dinâmica de Campo Elétrico", fontsize=14)
ax.set_xlabel("Eixo X")
ax.set_ylabel("Eixo Y")