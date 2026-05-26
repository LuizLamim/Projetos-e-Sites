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

# Plota cada uma das funções com cores e rótulos específicos
plt.plot(x, f, label="f(x) = cos(x)", color="blue", linewidth=2)
plt.plot(x, g, label="g(x) = sen(x) / x", color="darkorange", linewidth=2)
plt.plot(x, h, label="h(x) = 1 / cos(x)", color="crimson", linewidth=2)

# 4. Customização estética do gráfico
plt.title("Gráfico das Funções: f(x), g(x) e h(x)", fontsize=14, fontweight="bold")
plt.xlabel("Eixo X", fontsize=12)
plt.ylabel("Eixo Y", fontsize=12)

# Limita o eixo Y para que a função h(x) não estoure a escala visual do gráfico
plt.ylim(-4, 4)

# Adiciona linhas de referência nos eixos zero (X e Y)
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
plt.axvline(0, color="black", linewidth=0.8, linestyle="--")

# Ajusta os marcadores do eixo X para mostrar termos em função de Pi (opcional, melhora a leitura)
plt.xticks(
    [-3 * np.pi, -2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi, 3 * np.pi],
    [r"$-3\pi$", r"$-2\pi$", r"$-\pi$", "0", r"$\pi$", r"$2\pi$", r"$3\pi$"],
)

# Adiciona a legenda e a grade ao fundo
plt.legend(loc="upper right", fontsize=11)
plt.grid(True, linestyle=":", alpha=0.6)

# 5. Exibe o gráfico na tela
plt.tight_layout()
plt.show()