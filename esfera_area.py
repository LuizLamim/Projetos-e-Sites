import math

def calcular_area_esfera(raio):
    """Calcula a área da superfície de uma esfera dado o seu raio."""
    area = 4 * math.pi * (raio ** 2)
    return area

# Entrada do usuário
try:
    raio_input = float(input("Digite o raio da esfera: "))

    if raio_input < 0:
        print("O raio não pode ser negativo.")
    else:
        resultado = calcular_area_esfera(raio_input)
        print(f"A área da superfície da esfera com raio {raio_input} é: {resultado:.2f}")

except ValueError:
    print("Por favor, digite um valor numérico válido.")