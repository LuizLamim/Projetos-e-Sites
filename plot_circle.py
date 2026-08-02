import numpy as np
import matplotlib.pyplot as plt

# 1. Definir os ângulos de 0 a 2*pi (uma volta completa)
theta = np.linspace(0, 2 * np.pi, 150)

# 2. Definir o raio da circunferência (sqrt(25) = 5)
raio = 5

# 3. Calcular as coordenadas x e y usando equações paramétricas
x = raio * np.cos(theta)
y = raio * np.sin(theta)

# 4. Criar a figura e plotar o gráfico
plt.figure(figsize=(6, 6)) # Tamanho quadrado para não distorcer
plt.plot(x, y, label=r'$x^2 + y^2 = 25$', color='blue', linewidth=2)

# 5. Formatar o gráfico (Eixos, grade e título)
plt.title("Gráfico da Circunferência: $x^2 + y^2 = 25$", fontsize=14)
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")

# Desenhar as linhas dos eixos x e y cruzando no zero
plt.axhline(0, color='black', linewidth=1.2)
plt.axvline(0, color='black', linewidth=1.2)

# Adicionar uma grade para facilitar a visualização
plt.grid(color='gray', linestyle='--', linewidth=0.5)

# Garantir que a proporção dos eixos seja igual (1:1)
# Sem isso, o círculo pareceria uma elipse achatada
plt.axis('equal')