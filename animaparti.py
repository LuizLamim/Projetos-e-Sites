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

# --- Configuração do Gráfico e Animação (Matplotlib) ---
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, TAMANHO_CAIXA)
ax.set_ylim(0, TAMANHO_CAIXA)
ax.set_aspect('equal') # Mantém a caixa quadrada no visual
ax.set_title('Simulação de Gás Ideal: Colisões de Partículas')
# Remove as marcas dos eixos para um visual mais limpo
ax.set_xticks([])
ax.set_yticks([])

# Criar os objetos visuais das partículas (círculos)
particulas_visuais = [Circle(posicoes[i], RAIO_PARTICULA, color='navy', edgecolor='white') for i in range(N_PARTICULAS)]
for particula in particulas_visuais:
    ax.add_patch(particula)

# --- A Lógica da Física (Coração da Simulação) ---
def atualizar_simulacao(frame):
    global posicoes, velocidades

    # 1. Atualizar Posições (Movimento Retilíneo Uniforme entre colisões)
    posicoes += velocidades * DT

    # 2. Tratar Colisões com as Paredes (Paredes perfeitamente elásticas)
    # Parede Esquerda/Direita (Eixo X)
    # Se a posição X + Raio ultrapassar a caixa, inverte a velocidade X
    mask_parede_x = (posicoes[:, 0] <= RAIO_PARTICULA) | (posicoes[:, 0] >= TAMANHO_CAIXA - RAIO_PARTICULA)
    velocidades[mask_parede_x, 0] *= -1
    
    # Parede Inferior/Superior (Eixo Y)
    mask_parede_y = (posicoes[:, 1] <= RAIO_PARTICULA) | (posicoes[:, 1] >= TAMANHO_CAIXA - RAIO_PARTICULA)
    velocidades[mask_parede_y, 1] *= -1

    # 3. Tratar Colisões Partícula-Partícula (Cálculo O(N²))
    # Iteração sobre todos os pares únicos de partículas
    for i in range(N_PARTICULAS):
        for j in range(i + 1, N_PARTICULAS):
            dr = posicoes[i] - posicoes[j]
            dist_sq = np.dot(dr, dr) # Distância ao quadrado (evita raiz quadrada, mais rápido)
            
            # Se a distância quadrada for menor que o diâmetro ao quadrado, colidiram
            if dist_sq < (2 * RAIO_PARTICULA)**2:
                # Elas colidiram!
                dist = np.sqrt(dist_sq)
                n_unitario = dr / dist # Vetor normal unitário da colisão

                # Velocidade relativa
                dv = velocidades[i] - velocidades[j]
                
                # Velocidade relativa projetada na direção normal (vn)
                # Se vn < 0, as partículas estão se aproximando (aplica a colisão)
                vn = np.dot(dv, n_unitario)

                if vn < 0:
                    # Fórmula da colisão elástica simplificada para massas iguais
                    # Aplica a troca de momentum apenas na componente normal
                    delta_v = vn * n_unitario
                    velocidades[i] -= delta_v
                    velocidades[j] += delta_v

    # 4. Atualizar o Visual na Tela
    for i in range(N_PARTICULAS):
        particulal_visual = particulas_visuais[i]
        particulal_visual.center = posicoes[i]

    # Retorna a lista de objetos atualizados para o Matplotlib
    return particulas_visuais

