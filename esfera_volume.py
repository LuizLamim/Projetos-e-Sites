import math

def calcular_volume_esfera(raio):
    # Fórmula: (4/3) * pi * r^3
    volume = (4/3) * math.pi * (raio ** 3)
    return volume

# Solicita o raio ao usuário
try:
    r = float(input("Digite o raio da esfera: "))

    if r < 0:
        print("O raio não pode ser negativo.")
    else:
        resultado = calcular_volume_esfera(r)
        print(f"O volume da esfera com raio {r} é: {resultado:.2f}")b
except ValueError: