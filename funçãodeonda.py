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

# 2. Criar a malha de coordenadas (plano xz, onde y = 0)
limite = 20 # Tamanho do grid em raios de Bohr
pontos = 500
x = np.linspace(-limite, limite, pontos)
z = np.linspace(-limite, limite, pontos)
X, Z = np.meshgrid(x, z)
Y = 0 

# Converter coordenadas cartesianas para esféricas
R = np.sqrt(X**2 + Y**2 + Z**2)

# Evitar erro de divisão por zero na origem (r=0)
Theta = np.zeros_like(R)
mascara = R > 0
Theta[mascara] = np.arccos(Z[mascara] / R[mascara]) # Ângulo polar
Phi = np.arctan2(Y, X) # Ângulo azimutal

# 3. Calcular a função de onda e a densidade de probabilidade
psi = funcao_onda_hidrogenio(n, l, m, R, Theta, Phi)
densidade_probabilidade = np.abs(psi)**2

# 4. Plotar o resultado
plt.figure(figsize=(8, 6))
# Usamos o colormap 'inferno' que destaca bem as regiões de alta densidade
img = plt.imshow(densidade_probabilidade, extent=[-limite, limite, -limite, limite], 
                 origin='lower', cmap='inferno')

plt.colorbar(img, label='Densidade de Probabilidade $|\psi|^2$')
plt.title(f'Corte no plano XZ do Orbital do Hidrogênio (n={n}, l={l}, m={m})')
plt.xlabel('Eixo X (Raios de Bohr, $a_0$)')
plt.ylabel('Eixo Z (Raios de Bohr, $a_0$)')

# Ajustar o layout e mostrar
plt.tight_layout()
plt.show()