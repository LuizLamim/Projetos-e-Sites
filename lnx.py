import numpy as np
import matplotlib.pyplot as plt

# 1. Definir o intervalo de x
# Nota: O logaritmo natural não é definido para x <= 0.
# Começamos de 0.1 para evitar erros matemáticos e mostrar a curva descendo.
x = np.linspace(0.1, 10, 400)
y = np.log(x)