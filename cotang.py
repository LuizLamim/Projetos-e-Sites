import numpy as np
import matplotlib.pyplot as plt

# 1. Definir o intervalo de x (de -2π a 2π com 1000 pontos para suavidade)
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)


# 2. Calcular a cotangente (1 / tangente)
# Usamos um pequeno aviso de ignorar divisão por zero para evitar poluir o terminal
with np.errstate(divide='ignore'):
    y = 1 / np.tan(x)

# 3. Lidar com as assíntotas
# Cortamos os valores que explodem para o infinito para não estragar o gráfico
limite = 10
y[y > limite] = np.nan
y[y < -limite] = np.nan

# 4. Criar e configurar o gráfico
plt.figure(figsize=(10, 6))
plt.plot(x, y, label=r'$\cot(x)$', color='blue', linewidth=2)

# Configurar os eixos centrais (x=0 e y=0)
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

# Limitar a altura do eixo Y para melhor visualização
plt.ylim(-5, 5)

# Configurar as marcações do eixo X para mostrar múltiplos de π
pi_ticks = [-2*np.pi, -np.pi, 0, np.pi, 2*np.pi]
pi_labels = [r'$-2\pi$', r'$-\pi$', '0', r'$\pi$', r'$2\pi$']
plt.xticks(pi_ticks, pi_labels)

# Adicionar título, rótulos e grade
plt.title('Gráfico da Função Cotangente: $y = \cot(x)$', fontsize=14)
plt.xlabel('x (radianos)', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=12)

# Exibir o gráfico
plt.show()