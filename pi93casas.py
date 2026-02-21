import decimal

def calcular_pi(casas_decimais):
    # Define a precisão do cálculo. 
    # Adicionamos 5 casas extras como "gordura" para evitar erros de arredondamento no último dígito.
    decimal.getcontext().prec = casas_decimais + 5
    
    # Valores iniciais do algoritmo de Gauss-Legendre
    a = decimal.Decimal(1)
    b = decimal.Decimal(1) / decimal.Decimal(2).sqrt()
    t = decimal.Decimal(1) / decimal.Decimal(4)
    p = decimal.Decimal(1)
    
    # 10 repetições são mais que suficientes para calcular centenas de casas decimais precisas
    for _ in range(10):
        a_prox = (a + b) / 2
        b_prox = (a * b).sqrt()
        t_prox = t - p * (a - a_prox)**2
        p_prox = 2 * p
        
        a, b, t, p = a_prox, b_prox, t_prox, p_prox
        
    # Calcula o valor final de Pi
    pi = ((a + b)**2) / (4 * t)
    
    # Converte para texto para podermos cortar no tamanho exato solicitado
    pi_str = str(pi)
    
    # O corte pega "3." (2 caracteres) + a quantidade de casas decimais desejadas
    return pi_str[:casas_decimais + 2]

# Executando o programa
if __name__ == "__main__":
    casas = 93
    meu_pi = calcular_pi(casas)
    
    print(f"O número Pi com exatamente {casas} casas decimais é:\n")
    print(meu_pi)
    
    # Apenas para confirmar se o tamanho está correto:
    casas_calculadas = len(meu_pi.split('.')[1])
    print(f"\nVerificação: O número gerado possui {casas_calculadas} casas decimais.")