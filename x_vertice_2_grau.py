def calcular_x_vertice():

    try:
        # Recebe os coeficientes do usuário
        a = float(input("Digite o valor de a: "))
        b = float(input("Digite o valor de b: "))
        c = float(input("Digite o valor de c: ")) # O 'c' não afeta o Xv, mas define a função

        # Validação: se a for 0, não é uma equação do 2º grau
        if a == 0:
            print("\nErro: O coeficiente 'a' não pode ser igual a zero em uma função do 2º grau.")
            return

        # Aplica a fórmula: Xv = -b / (2 * a)
        x_vertice = -b / (2 * a)
        
        print("\n" + "="*30)
        print(f"Para a função f(x) = {a}x² + {b}x + {c}:")
        print(f"O X do vértice (Xv) é: {x_vertice:.2f}")
        print("="*30)
        
    except ValueError:
        print("\nErro: Por favor, digite apenas números válidos.")

    