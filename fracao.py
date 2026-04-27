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