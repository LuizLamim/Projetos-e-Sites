import matplotlib.pyplot as plt
import numpy as np

# 1. Definindo o intervalo de x (de -3pi a 3pi)
x = np.linspace(-3 * np.pi, 3 * np.pi, 1000)

# 2. Definindo as funções
# f(x) = cos(x)
f = np.cos(x)

# g(x) = sin(x) / x
# Usamos np.where para evitar o aviso de divisão por zero caso x seja exatamente 0
g = np.where(x == 0, 1.0, np.sin(x) / x)

# h(x) = 1 / cos(x)
cos_x = np.cos(x)
h = 1 / cos_x
# Mascaramos os valores onde cos(x) é muito próximo de zero para evitar linhas verticais feias ligando +infinito a -infinito
h[abs(cos_x) < 0.05] = np.nan

# 3. Configurando a figura do gráfico
plt.figure(figsize=(12, 6))