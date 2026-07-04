# Programa para calcular a área de um trapézio

print("--- Calculadora de Área do Trapézio ---")

# Solicitando os dados ao usuário
base_maior = float(input("Digite o comprimento da base maior (B): "))
base_menor = float(input("Digite o comprimento da base menor (b): "))
altura = float(input("Digite a altura do trapézio (h): "))

# Aplicando a fórmula: A = ((B + b) * h) / 2
area = ((base_maior + base_menor) * altura) / 2