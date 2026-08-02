import numpy as np
import matplotlib.pyplot as plt

# 1. Definir os ângulos de 0 a 2*pi (uma volta completa)
theta = np.linspace(0, 2 * np.pi, 150)

# 2. Definir o raio da circunferência (sqrt(25) = 5)
raio = 5

# 3. Calcular as coordenadas x e y usando equações paramétricas
x = raio * np.cos(theta)
y = raio * np.sin(theta)