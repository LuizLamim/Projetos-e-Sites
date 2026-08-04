def calcular_soma_porcentagens():
    print("--- Calculadora de Soma de Porcentagens ---\n")

    # Recebe as três porcentagens do usuário
    try:
        p1 = float(input("Digite a primeira porcentagem (%): "))
        p2 = float(input("Digite a segunda porcentagem (%): "))
        p3 = float(input("Digite a terceira porcentagem (%): "))

        # Soma os valores informados
        soma_total = p1 + p2 + p3

        # Exibe os resultados
        print("\n--- Resultados ---")
        print(f"Soma bruta: {soma_total:.2f}%")

        # Exemplo prático: caso queira ver quanto essa soma representa de um determinado valor
        calcular_valor = input(
            "\nDeseja aplicar essa soma a um valor total? (s/n): "
        ).lower()

        if calcular_valor == "s":
            valor_total = float(input("Digite o valor total (R$): "))
            resultado_valor = (soma_total / 100) * valor_total
            print(
                f"\n{soma_total:.2f}% de R$ {valor_total:.2f} equivale a: R$ {resultado_valor:.2f}"
            )

    except ValueError:
        print(
            "\nErro: Por favor, digite apenas números válidos (use ponto para decimais, ex: 10.5)."
        )


# Executa o programa
calcular_soma_porcentagens()