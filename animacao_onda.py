import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Configurando o espaço do gráfico
fig, ax = plt.subplots()
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.5, 1.5)
ax.set_title('Animação de Onda Senoidal')

# Criando a linha inicial (vazia)
linha, = ax.plot([], [], lw=2, color='#C44E52')

# Função que prepara o fundo de cada frame
def iniciar():
    linha.set_data([], [])
    return linha,

# Função que calcula os dados de cada frame (a passagem do tempo)
def animar(i):
    x = np.linspace(0, 2 * np.pi, 1000)
    # A fórmula da onda: o 'i' desloca a onda para a esquerda criando o movimento
    y = np.sin(x - (i * 0.1)) 
    linha.set_data(x, y)
    return linha,

# Gerando a animação (200 frames, intervalo de 20 milissegundos)
ani = animation.FuncAnimation(fig, animar, init_func=iniciar,
                              frames=200, interval=20, blit=True)

# Exibe a animação rodando em loop
plt.show()