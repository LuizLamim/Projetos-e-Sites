def calcular_potencia_base_10():
    print("--- Calculadora de Potência (Base 10) ---")

    try:
        # Solicita o expoente ao usuário (aceita números decimais e negativos)
        entrada = input("Digite o valor do expoente (x) para 10^x: ")
        
        # Converte a entrada para float para permitir expoentes decimais (ex: 2.5)
        expoente = float(entrada)
        
        # Calcula a potência
        resultado = 10 ** expoente

        # Formata a saída para ficar mais limpa se o número for inteiro
        if expoente.is_integer():
            print(f"\nResultado: 10^{int(expoente)} = {int(resultado)}")
        else:
            print(f"\nResultado: 10^{expoente} = {resultado}")
            
    except ValueError:
        print("\nErro: Por favor, digite um número válido.")

# Executa a função principal
if __name__ == "__main__":
    calcular_potencia_base_10()