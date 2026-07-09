import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt

# 1. Define os valores de x (de -10 a 10, gerando 400 pontos para uma curva suave)
x = np.linspace(-10, 10, 400)

# 2. Calcula os valores de y para a função x^3
y = x**3

# 3. Configura e plota o gráfico
plt.plot(x, y, label='$f(x) = x^3$', color='blue', linewidth=2)

