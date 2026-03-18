def calcular_potencia():
    print("--- Calculadora de Potência ---")

    try:
        # Solicita o número base (x) e converte para decimal
        x = float(input("Digite o número base (x): "))
        
        # Solicita o expoente (y) e converte para decimal
        y = float(input("Digite o expoente (y): "))
        
        # O operador ** é usado para exponenciação em Python
        resultado = x ** y
        
        # Exibe o resultado formatado
        print(f"\nO resultado de {x} elevado a {y} é: {resultado}")
    
    except ValueError:
        print("\nErro: Por favor, digite apenas números válidos.")

# Executa a função
if __name__ == "__main__":
    calcular_potencia()