import numpy as np
import matplotlib.pyplot as plt

# 1. Definindo o intervalo de x
# Geramos 400 pontos linearmente espaçados entre -1.5 e 1.5
x = np.linspace(-1.5, 1.5, 400)

# 2. Calculando a equação
y = x**15

# 3. Configurando a figura
plt.figure(figsize=(9, 6))
plt.plot(x, y, label='$y = x^{15}$', color='blue', linewidth=2)

# 4. Personalizando o gráfico (títulos e eixos)
plt.title('Gráfico da Equação $y = x^{15}$')
plt.xlabel('x')
plt.ylabel('y')

# Adicionando linhas de grade e eixos centrais
plt.grid(True, linestyle='--', alpha=0.6)
plt.axhline(0, color='black', linewidth=1) # Eixo X
plt.axvline(0, color='black', linewidth=1) # Eixo Y

# 5. Exibindo a legenda e o gráfico final
plt.legend()
plt.show()