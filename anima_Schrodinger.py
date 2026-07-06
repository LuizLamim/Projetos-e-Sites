import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# Definindo constantes (unidades naturais: hbar = 1, m = 1, omega = 1)
x = np.linspace(-5, 5, 500)

# Funções de onda dos autoestados (Estado fundamental e 1º estado excitado)
def psi_0(x):
    """Estado fundamental do oscilador harmônico"""
    return (1.0 / np.pi)**0.25 * np.exp(-x**2 / 2.0)

def psi_1(x):
    """Primeiro estado excitado"""
    return (1.0 / np.pi)**0.25 * np.sqrt(2.0) * x * np.exp(-x**2 / 2.0)


# Configuração da figura e dos eixos
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(-5, 5)
ax.set_ylim(-1, 1.2)
ax.set_xlabel('Posição (x)')
ax.set_ylabel('Amplitude')
ax.set_title('Evolução Temporal - Equação de Schrödinger (Oscilador Harmônico)')
ax.grid(True, linestyle='--', alpha=0.6)