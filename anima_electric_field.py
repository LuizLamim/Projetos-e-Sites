import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- Configurações Iniciais da Simulação ---
# Constante eletrostática (normalizada para 1 para simplificar a escala)
K = 1.0  

# Configuração do espaço (Grade de pontos onde o campo será calculado)
X, Y = np.meshgrid(np.linspace(-5, 5, 20), np.linspace(-5, 5, 20))