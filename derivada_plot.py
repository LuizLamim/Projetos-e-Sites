import matplotlib.pyplot as plt
import numpy as np

# 1. Definir o intervalo de x
x = np.linspace(-10, 10, 400)

# 2. Definir as funções
f = 2 * x**2 + 5
g = 4 * x

# 3. Criar o gráfico
plt.figure(figsize=(8, 6))
plt.plot(x, f, label='$f(x) = 2x^2 + 5$', color='blue', linewidth=2)
plt.plot(x, g, label='$g(x) = 4x$', color='red', linestyle='--', linewidth=2)