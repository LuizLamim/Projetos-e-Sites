from fractions import Fraction

def somar_fracoes():
    print("--- Programa para Somar Frações ---")
    
    # Solicita ao usuário que insira as frações
    frac1_input = input("Digite a primeira fração (ex: 1/2): ")
    frac2_input = input("Digite a segunda fração (ex: 3/4): ")

    ry:
        # Converte as entradas de texto em objetos matemáticos Fraction
        f1 = Fraction(frac1_input)
        f2 = Fraction(frac2_input)

        # O Python soma e simplifica a fração automaticamente
        resultado = f1 + f2

        print("\n--- Resultado ---")
        print(f"{f1} + {f2} = {resultado}")

    except ValueError:
        print("\nErro: Formato inválido. Por favor, insira as frações no formato correto (ex: 1/2, 3/4).")