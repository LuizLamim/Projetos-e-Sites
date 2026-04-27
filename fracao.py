import math

def somar_fracoes():
    print("--- Calculadora de Soma de Frações ---\n")
    
    # Coletando os dados da PRIMEIRA fração
    print("Primeira Fração:")
    num1 = int(input("Digite o numerador (número de cima): "))
    den1 = int(input("Digite o denominador (número de baixo): "))
    
    # Coletando os dados da SEGUNDA fração
    print("\nSegunda Fração:")
    num2 = int(input("Digite o numerador (número de cima): "))
    den2 = int(input("Digite o denominador (número de baixo): "))
    
    # Validação de segurança: o denominador nunca pode ser zero
    if den1 == 0 or den2 == 0:
        print("\nErro: O denominador não pode ser igual a zero!")
        return
    
    # Passo 1: Aplicar a regra de soma de frações
    num_resultado = (num1 * den2) + (num2 * den1)
    den_resultado = den1 * den2
    
    # Passo 2: Simplificar a fração resultante usando o MDC
    mdc = math.gcd(num_resultado, den_resultado)
    num_simplificado = num_resultado // mdc
    den_simplificado = den_resultado // mdc
    
    # Passo 3: Exibir o resultado
    print("\n--- Resultado ---")
    print(f"A soma de {num1}/{den1} + {num2}/{den2} é:")

    # Se o denominador for 1, o resultado é um número inteiro, então ocultamos o "/1"
    if den_simplificado == 1:
        print(f"{num_simplificado}")
    elif num_simplificado == 0:
        print("0")
    else:
        print(f"{num_simplificado}/{den_simplificado}")

# Executa o programa
somar_fracoes()