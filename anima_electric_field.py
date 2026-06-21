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

# Elementos visuais que serão atualizados
# quiver: plota os vetores (setas) do campo
quiver = ax.quiver(X, Y, np.zeros_like(X), np.zeros_like(Y), color='white', scale=20)
# Desenho das cargas (esferas coloridas)
carga_pos_plot, = ax.plot([], [], 'ro', markersize=12, label='Carga + (Proton)')
carga_neg_plot, = ax.plot([], [], 'bo', markersize=12, label='Carga - (Elétron)')
ax.legend(loc='upper right')
ax.set_facecolor('#111111') # Fundo escuro para destacar as setas

# --- Função de Animação ---
def atualizar(frame):
    # Define o movimento das cargas ao longo do tempo (usando seno e cosseno)
    # A carga positiva orbita e a negativa se move em linha reta
    pos_positiva = [2 * np.cos(frame * 0.05), 2 * np.sin(frame * 0.05)]
    pos_negativa = [-2 * np.cos(frame * 0.03), 0]
    
    # Valores das cargas (em Coulombs arbitrários)
    q_positiva = 5.0
    q_negativa = -5.0
    
    # Calcula o campo de cada uma
    Ex1, Ey1 = calcular_campo_carga(q_positiva, pos_positiva, X, Y)
    Ex2, Ey2 = calcular_campo_carga(q_negativa, pos_negativa, X, Y)
    
    # Princípio da Superposição: o campo total é a soma dos campos individuais
    Ex_total = Ex1 + Ex2
    Ey_total = Ey1 + Ey2
    
    # Normaliza os vetores para que todas as setas tenham o mesmo tamanho,
    # mudando apenas a direção (torna o gráfico mais limpo)
    magnitude = np.sqrt(Ex_total**2 + Ey_total**2)
    magnitude[magnitude == 0] = 1e-6
    Ex_norm = Ex_total / magnitude
    Ey_norm = Ey_total / magnitude
    
    # Atualiza as posições dos desenhos das cargas
    carga_pos_plot.set_data([pos_positiva[0]], [pos_positiva[1]])
    carga_neg_plot.set_data([pos_negativa[0]], [pos_negativa[1]])
    
    # Atualiza as setas do campo elétrico
    quiver.set_UVC(Ex_norm, Ey_norm)
    
    return quiver, carga_pos_plot, carga_neg_plot

# --- Executa a Animação ---
# frames: número de iterações, interval: tempo em milissegundos entre frames
anim = FuncAnimation(fig, atualizar, frames=200, interval=30, blit=True)

plt.show()