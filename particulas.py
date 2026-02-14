import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Configurações iniciais
N_PARTICULAS = 25
TAMANHO_TANQUE = 10
RAIO_PARTICULA = 0.3
VELOCIDADE_INICIAL = 0.15

class SimulacaoGas:
    def __init__(self, n, tanque, raio):
        self.n = n
        self.tanque = tanque
        self.raio = raio
        
        # Posições aleatórias (x, y)
        self.pos = np.random.uniform(raio, tanque - raio, (n, 2))
        
        # Velocidades aleatórias
        angulos = np.random.uniform(0, 2 * np.pi, n)
        self.vel = np.column_stack((np.cos(angulos), np.sin(angulos))) * VELOCIDADE_INICIAL

    def atualizar(self):
        # 1. Mover partículas
        self.pos += self.vel

        # 2. Colisão com as paredes (Inversão de vetor)
        for i in range(self.n):
            if self.pos[i, 0] <= self.raio or self.pos[i, 0] >= self.tanque - self.raio:
                self.vel[i, 0] *= -1
            if self.pos[i, 1] <= self.raio or self.pos[i, 1] >= self.tanque - self.raio:
                self.vel[i, 1] *= -1