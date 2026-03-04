import matplotlib.pyplot as plt
import numpy as np

# 1. Definir o intervalo de x (x deve ser maior que 0 para logaritmos)
# Vamos de 0.1 até 10 para evitar o erro de log(0)
x = np.linspace(0.1, 10, 400)