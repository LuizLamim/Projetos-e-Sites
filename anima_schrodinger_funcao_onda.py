import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- Constantes do Sistema Quântico ---
# Estamos usando unidades atômicas (hbar = 1, massa = 1) para simplificar a computação
L = 1.0          # Largura do poço de potencial
hbar = 1.0       # Constante de Planck reduzida
m = 1.0          # Massa da partícula

# --- Discretização do Espaço ---
N = 500          # Número de pontos na malha espacial
x = np.linspace(0, L, N)

# --- Funções Analíticas ---
def psi_n(n, x):
    """Retorna a função de onda espacial para o n-ésimo estado no poço infinito."""
    return np.sqrt(2.0 / L) * np.sin(n * np.pi * x / L)

def energia_n(n):
    """Calcula a energia do n-ésimo estado."""
    return (n**2 * np.pi**2 * hbar**2) / (2.0 * m * L**2)

# Frequências angulares associadas a cada estado (omega = E / hbar)
omega_1 = energia_n(1) / hbar
omega_2 = energia_n(2) / hbar

# --- Configuração da Interface Gráfica ---
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, L)
ax.set_ylim(-3, 3)
ax.set_xlabel('Posição $x$ na Caixa')
ax.set_ylabel('Amplitude')
ax.set_title('Animação da Função de Onda de Schrödinger (Superposição)')
ax.grid(True, linestyle='--', alpha=0.5)

# Instanciando as linhas do gráfico que serão animadas
line_real, = ax.plot([], [], label='Parte Real $\Re(\Psi)$', color="#FC05B2", alpha=0.7)
line_imag, = ax.plot([], [], label='Parte Imaginária $\Im(\Psi)$', color="#00B7FF", alpha=0.7)
line_prob, = ax.plot([], [], label='Densidade de Probabilidade $|\Psi|^2$', color="#E8A411", linewidth=2.5)
ax.legend(loc='upper right')

# --- Funções da Animação ---
def init():
    """Inicializa as linhas vazias no primeiro frame."""
    line_real.set_data([], [])
    line_imag.set_data([], [])
    line_prob.set_data([], [])
    return line_real, line_imag, line_prob

def update(t):
    """Atualiza a função de onda para um determinado tempo t."""
    # Cálculo da superposição com evolução temporal (fases complexas)
    estado_1 = (1/np.sqrt(2)) * psi_n(1, x) * np.exp(-1j * omega_1 * t)
    estado_2 = (1/np.sqrt(2)) * psi_n(2, x) * np.exp(-1j * omega_2 * t)
    
    psi_total = estado_1 + estado_2

    # Atualizando os dados no gráfico
    line_real.set_data(x, np.real(psi_total))
    line_imag.set_data(x, np.imag(psi_total))
    line_prob.set_data(x, np.abs(psi_total)**2) # A probabilidade é o módulo quadrado
    
    return line_real, line_imag, line_prob

# Geração dos frames de tempo e execução da animação
vetor_tempo = np.linspace(0, 10, 400)
ani = FuncAnimation(fig, update, frames=vetor_tempo, init_func=init, 
                    blit=True, interval=40)

# Renderiza a janela
plt.show()