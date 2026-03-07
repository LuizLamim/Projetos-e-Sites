import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

# --- Parâmetros da Simulação ---
N_PARTICULAS = 75     # Número de partículas no recipiente
TAMANHO_CAIXA = 10.0 # O recipiente é uma caixa quadrada (L x L)
RAIO_PARTICULA = 0.15 # Raio visual (influencia colisões partícula-partícula)
MASSA = 1.0           # Massa idêntica para todas as partículas
V0 = 5.0              # Fator de escala da velocidade inicial (simula "temperatura")
DT = 0.02             # Passo de tempo da simulação (quão rápido o tempo passa)
INTERVALO_MS = 25     # Intervalo entre quadros da animação em milissegundos

# --- Inicialização das Partículas ---

# 1. Velocidades: Geradas em direções aleatórias
# Usamos distribuição normal para simular Maxwell-Boltzmann em 2D
velocidades = np.random.randn(N_PARTICULAS, 2) * (V0 / np.sqrt(2))

# 2. Posições: Aleatórias, mas garantindo que não se sobreponham inicialmente
# Criamos uma grade para garantir o espaçamento inicial
posicoes = np.zeros((N_PARTICULAS, 2))
grid_dim = int(np.sqrt(N_PARTICULAS)) + 1
x_grid = np.linspace(RAIO_PARTICULA * 2, TAMANHO_CAIXA - RAIO_PARTICULA * 2, grid_dim)
y_grid = np.linspace(RAIO_PARTICULA * 2, TAMANHO_CAIXA - RAIO_PARTICULA * 2, grid_dim)
pontos_grade = np.vstack([np.repeat(x_grid, grid_dim), np.tile(y_grid, grid_dim)]).T
indices = np.random.choice(range(len(pontos_grade)), N_PARTICULAS, replace=False)
posicoes = pontos_grade[indices]

