def exibir_menu():
    print("\n--- Calculadora Python ---")
    print("1. Soma (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    print("5. Potência (^)")
    print("0. Sair")

def calcular():
    while True:
        exibir_menu()
        
        escolha = input("\nEscolha uma operação (0-5): ")
        
        if escolha == '0':
            print("Saindo do programa. Até mais!")
            break
            
        if escolha not in ['1', '2', '3', '4', '5']:
            print("Opção inválida! Tente novamente.")
            continue
        
        try:
            # Captura os números
            x = float(input("Digite o primeiro número (x): "))
            y = float(input("Digite o segundo número (y): "))
            
            resultado = None
            operacao = ""

            # Lógica das 4 operações
            if escolha == '1':
                resultado = x + y
                operacao = "soma"
            elif escolha == '2':
                resultado = x - y
                operacao = "subtração"
            elif escolha == '3':
                resultado = x * y
                operacao = "multiplicação"
            elif escolha == '4':
                if y == 0:
                    print("Erro: Não é possível dividir por zero.")
                    continue
                resultado = x / y
                operacao = "divisão"
            elif escolha == '5':
                resultado = x ** y
                operacao = "potência"
            
            # Exibe o resultado se foi calculado com sucesso
            if resultado is not None:
                print(f"O resultado da {operacao} entre {x} e {y} é: {resultado}")
                
        except ValueError:
            print("Erro: Entrada inválida. Por favor, insira apenas números.")

if __name__ == "__main__":
    calcular()