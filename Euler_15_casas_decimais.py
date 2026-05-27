from decimal import Decimal, getcontext
import math

def calcular_euler(casas_decimais):
    # Define a precisão do contexto para o número de casas + algumas extras
    # para evitar erros de arredondamento durante o cálculo
    getcontext().prec = casas_decimais + 2
    
    e = Decimal(0)
    for n in range(50):  # 50 iterações são mais que suficientes para 15 casas
        e += Decimal(1) / Decimal(math.factorial(n))
        
    # Retorna formatado para o número de casas desejado
    return format(e, f'.{casas_decimais}f')

# Execução
resultado = calcular_euler(20)
print(f"O valor de e com 20 casas decimais é: {resultado}")