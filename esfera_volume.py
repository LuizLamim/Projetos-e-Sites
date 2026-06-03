import math

def calcular_volume_esfera(raio):
    # Fórmula: (4/3) * pi * r^3
    volume = (4/3) * math.pi * (raio ** 3)
    return volume

# Solicita o raio ao usuário
try:
    r = float(input("Digite o raio da esfera: "))