import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 1. Definir os 16 vértices do tesseract (coordenadas de -1 a 1 em 4D)
vertices = []
for i in range(16):
    x = -1 if (i & 1) == 0 else 1
    y = -1 if (i & 2) == 0 else 1
    z = -1 if (i & 4) == 0 else 1
    w = -1 if (i & 8) == 0 else 1
    vertices.append(np.array([x, y, z, w]))

# 2. Definir as 32 arestas conectando os vértices
# Uma aresta existe se os vértices diferem em exatamente 1 bit em binário
edges = []
for i in range(16):
    for j in range(i + 1, 16):
        if bin(i ^ j).count('1') == 1:
            edges.append((i, j))

# 3. Configurar a figura 3D do Matplotlib
fig = plt.figure(figsize=(8, 8), facecolor='black')
ax = fig.add_subplot(111, projection='3d')
ax.set_facecolor('black')

# Remover eixos para um visual mais limpo
ax.axis('off')
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])

# Inicializar as linhas (arestas) e os pontos (vértices)
lines = [ax.plot([], [], [], color='cyan', lw=1.5, alpha=0.8)[0] for _ in edges]
scatter = ax.scatter([], [], [], color='magenta', s=40)


# 4. Função de atualização para cada quadro (frame) da animação
def update(frame):
    angle = frame * 0.03  # Velocidade da rotação
    
    # Rotação no plano XW
    cos_a, sin_a = np.cos(angle), np.sin(angle)
    # Rotação no plano YW (ligeiramente diferente para um efeito legal)
    cos_b, sin_b = np.cos(angle * 0.8), np.sin(angle * 0.8)

    projected_vertices = []
    
    for v in vertices:
        # Aplicar rotação XW
        x = v[0] * cos_a - v[3] * sin_a
        y = v[1]
        z = v[2]
        w = v[0] * sin_a + v[3] * cos_a

        # Aplicar rotação YW
        y_new = y * cos_b - w * sin_b
        w_new = y * sin_b + w * cos_b

        # Projeção em Perspectiva (4D para 3D)
        # O eixo W atua como a "distância" focal
        distance = 3
        w_factor = 1 / (distance - w_new)

        px = x * w_factor
        py = y_new * w_factor
        pz = z * w_factor

        projected_vertices.append([px, py, pz])

    projected_vertices = np.array(projected_vertices)

    # Atualizar as posições das arestas
    for i, edge in enumerate(edges):
        p1 = projected_vertices[edge[0]]
        p2 = projected_vertices[edge[1]]
        lines[i].set_data([p1[0], p2[0]], [p1[1], p2[1]])
        lines[i].set_3d_properties([p1[2], p2[2]])

    # Atualizar as posições dos vértices
    scatter._offsets3d = (projected_vertices[:, 0], projected_vertices[:, 1], projected_vertices[:, 2])

    return lines + [scatter]

# 5. Gerar a animação
ani = animation.FuncAnimation(fig, update, frames=300, interval=30, blit=False)

# Exibir a janela com a animação rodando
plt.show()

# Nota: Se quiser salvar como GIF/MP4, comente o plt.show() e descomente abaixo:
# ani.save('tesseract.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
# Fazer no Futuro