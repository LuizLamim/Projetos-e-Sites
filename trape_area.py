def calcular_area_trapezio(base_maior, base_menor, altura):
    """Calcula a área de um trapézio dado as bases e a altura."""
    return ((base_maior + base_menor) * altura) / 2

# Entrada de dados
print("--- Calculadora de Área de Trapézio ---")

try:
    b_maior = float(input("Digite a base maior: "))
    b_menor = float(input("Digite a base menor: "))
    h = float(input("Digite a altura: "))

    # Cálculo e resultado
    area = calcular_area_trapezio(b_maior, b_menor, h)
    print(f"\nA área do trapézio é: {area:.2f}")
except ValueError:
    print("Por favor, digite apenas números válidos.")