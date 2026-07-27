import numpy as np
import matplotlib.pyplot as plt

def gerar_mandelbrot(xmin, xmax, ymin, ymax, largura, altura, max_iter):
    # Cria uma grade de coordenadas no plano complexo
    r1 = np.linspace(xmin, xmax, largura)
    r2 = np.linspace(ymin, ymax, altura)
    X, Y = np.meshgrid(r1, r2)