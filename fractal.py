import numpy as np
import matplotlib.pyplot as plt

def gerar_mandelbrot(xmin, xmax, ymin, ymax, largura, altura, max_iter):
    # Cria uma grade de coordenadas no plano complexo
    r1 = np.linspace(xmin, xmax, largura)
    r2 = np.linspace(ymin, ymax, altura)
    X, Y = np.meshgrid(r1, r2)

    # C é o nosso ponto no plano (Parte Real + Parte Imaginária)
    C = X + 1j * Y
    Z = np.zeros_like(C)

    # Matriz para armazenar a "cor" de cada pixel (número de iterações)
    fractal = np.zeros(C.shape, dtype=int)
    
    for i in range(max_iter):
        # Aplica a fórmula apenas aos pontos que ainda não "escaparam" (raio <= 2)
        mascara = np.abs(Z) <= 2
        
        # A famosa equação do fractal: Z = Z² + C
        Z[mascara] = Z[mascara]**2 + C[mascara]
        
        # Registra em qual iteração o ponto estava
        fractal[mascara] = i
        
    return fractal

# 1. Definindo a "janela da câmera"
xmin, xmax = -2.0, 1.0
ymin, ymax = -1.5, 1.5

print("Calculando o fractal... isso pode levar um ou dois segundos.")
# 2. Gerando a matriz (1000x1000 pixels, 100 iterações de profundidade)
matriz_fractal = gerar_mandelbrot(xmin, xmax, ymin, ymax, 1000, 1000, 100)