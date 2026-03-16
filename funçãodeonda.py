import numpy as np
import matplotlib.pyplot as plt
from scipy.special import sph_harm, genlaguerre
from math import factorial

def funcao_onda_hidrogenio(n, l, m, r, theta, phi):
    """
    Calcula a função de onda do átomo de hidrogênio.
    """
    a0 = 1.0 # Raio de Bohr em unidades atômicas
    
    # --- Parte Radial ---
    rho = 2.0 * r / (n * a0)
    # Constante de normalização radial
    norm_r = np.sqrt((2.0 / (n * a0))**3 * factorial(n - l - 1) / (2.0 * n * factorial(n + l)))
    # Polinômio associado de Laguerre
    laguerre = genlaguerre(n - l - 1, 2 * l + 1)(rho)
    R_nl = norm_r * np.exp(-rho / 2.0) * (rho**l) * laguerre
    
    # --- Parte Angular ---
    # Harmônicos esféricos (scipy usa phi para azimutal e theta para polar, a convenção física é o inverso, 
    # então passamos (m, l, phi, theta) para alinhar com a convenção scipy)
    Y_lm = sph_harm(m, l, phi, theta)
    
    return R_nl * Y_lm

# 1. Configurar os números quânticos
# Altere estes valores para ver diferentes orbitais!
# Exemplo: (1,0,0) = 1s | (2,1,0) = 2pz | (3,2,0) = 3dz^2
n = 3
l = 2
m = 0