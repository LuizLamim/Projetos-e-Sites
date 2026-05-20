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