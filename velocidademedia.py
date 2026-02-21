def calcular_velocidade_media():
    print("--- Calculadora de Velocidade Média ---")

    try:
        # Recebendo os dados do usuário
        distancia = float(input("Digite a distância percorrida (em km): "))
        tempo = float(input("Digite o tempo gasto (em horas): "))

        # Verificação para evitar divisão por zero
        if tempo <= 0:
            print("Erro: O tempo deve ser maior que zero.")
        else:
            # Cálculo da velocidade média
            velocidade_media = distancia / tempo
            
            # Exibindo o resultado formatado com 2 casas decimais
            print(f"\nA velocidade média é de {velocidade_media:.2f} km/h.")

    except ValueError:
        print("Erro: Por favor, insira apenas números válidos.")