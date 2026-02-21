import math

def calcular_perimetro():
    print("--- Calculadora de Perímetro de Circunferência ---")

    try:
        # 1. Recebe o valor do raio digitado pelo usuário
        raio_str = input("Digite o valor do raio: ")
        raio = float(raio_str) # Converte o texto para número decimal
        
        if raio < 0:
            print("O raio não pode ser um número negativo.")
            return
        
        perimetro = 2 * math.pi * raio

        print(f"\nResultado: O perímetro da circunferência é {perimetro:.2f}")

    except ValueError:
        print("\nErro: Por favor, digite um número válido (ex: 5 ou 2.5).")