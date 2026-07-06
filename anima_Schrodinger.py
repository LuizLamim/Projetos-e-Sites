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

# Inicializando as linhas que serão animadas
line_prob, = ax.plot([], [], label='Densidade de Probabilidade |Ψ|²', color='black', lw=2)
line_real, = ax.plot([], [], label='Parte Real Re(Ψ)', color='blue', alpha=0.7)
line_imag, = ax.plot([], [], label='Parte Imaginária Im(Ψ)', color='red', alpha=0.7, linestyle='--')

ax.legend(loc='upper right')

# Função de inicialização da animação
def init():
    line_prob.set_data([], [])
    line_real.set_data([], [])
    line_imag.set_data([], [])
    return line_prob, line_real, line_imag

# Função que atualiza cada frame da animação
def animate(t):
    # As energias são E_0 = 0.5 e E_1 = 1.5 (em unidades de hbar * omega)
    # Criamos uma superposição dos dois estados: Ψ(x,t) = (1/sqrt(2)) * (ψ0(x)e^{-i*E0*t} + ψ1(x)e^{-i*E1*t})
    psi_t = (1 / np.sqrt(2)) * (
        psi_0(x) * np.exp(-1j * 0.5 * t) + 
        psi_1(x) * np.exp(-1j * 1.5 * t)
    )
    
    # Calculando os componentes
    prob_density = np.abs(psi_t)**2
    real_part = np.real(psi_t)
    imag_part = np.imag(psi_t)
    
    # Atualizando os dados das linhas
    line_prob.set_data(x, prob_density)
    line_real.set_data(x, real_part)
    line_imag.set_data(x, imag_part)
    
    return line_prob, line_real, line_imag