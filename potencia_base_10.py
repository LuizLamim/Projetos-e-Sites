def calcular_potencia_base_10():
    print("--- Calculadora de Potência (Base 10) ---")

    try:
        # Solicita o expoente ao usuário (aceita números decimais e negativos)
        entrada = input("Digite o valor do expoente (x) para 10^x: ")
        
        # Converte a entrada para float para permitir expoentes decimais (ex: 2.5)
        expoente = float(entrada)
        
        # Calcula a potência
        resultado = 10 ** expoente