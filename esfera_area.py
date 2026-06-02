import math

def calcular_area_esfera(raio):
    """Calcula a área da superfície de uma esfera dado o seu raio."""
    area = 4 * math.pi * (raio ** 2)
    return area

# Entrada do usuário
try:
    raio_input = float(input("Digite o raio da esfera: "))