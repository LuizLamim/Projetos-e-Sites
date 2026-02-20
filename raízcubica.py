import math

def calcular_raiz_cubica():
    try:
        # Pede ao usuário para digitar um número
        entrada = input("Digite um número para calcular a raiz cúbica: ")
        numero = float(entrada)
        
        # Calcula a raiz cúbica usando a biblioteca math
        raiz = math.cbrt(numero)
        
        # Exibe o resultado formatado com 4 casas decimais
        print(f"A raiz cúbica de {numero} é {raiz:.4f}")

    except ValueError:
        print("Erro: Por favor, digite um número válido.")