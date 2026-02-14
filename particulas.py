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

        # 3. Colisão entre partículas (Simplificada)
        for i in range(self.n):
            for j in range(i + 1, self.n):
                dist = np.linalg.norm(self.pos[i] - self.pos[j])
                if dist < 2 * self.raio:
                    # Troca simples de velocidades (colisão elástica de massas iguais)
                    self.vel[i], self.vel[j] = self.vel[j].copy(), self.vel[i].copy()
                    
                    # Impede que as partículas fiquem presas uma dentro da outra
                    sobreposicao = 2 * self.raio - dist
                    direcao = (self.pos[i] - self.pos[j]) / dist
                    self.pos[i] += direcao * (sobreposicao / 2)
                    self.pos[j] -= direcao * (sobreposicao / 2)

# Configuração da figura
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, TAMANHO_TANQUE)
ax.set_ylim(0, TAMANHO_TANQUE)
ax.set_title("Simulação de Gás Ideal (Partículas em Tanque)")

sim = SimulacaoGas(N_PARTICULAS, TAMANHO_TANQUE, RAIO_PARTICULA)
scatter = ax.scatter(sim.pos[:, 0], sim.pos[:, 1], s=100, c='royalblue', edgecolors='black')