import math

def binomio_newton(n, var1='x', var2='y'):
    """
    Gera e exibe a expansão do Binômio de Newton para (var1 + var2)^n
    """
    if n < 0:
        return "Por favor, insira um expoente inteiro não-negativo (n >= 0)."
    
    if n == 0:
        return "1"
    
    termos = []
    
    for k in range(n + 1):
        # Calcula o coeficiente binomial: n! / (k! * (n-k)!)
        coeficiente = math.comb(n, k)
        
        # Define as potências de cada variável
        p_var1 = n - k
        p_var2 = k
        
        # Formata a parte das variáveis
        str_var1 = ""
        if p_var1 > 0:
            str_var1 = var1 if p_var1 == 1 else f"{var1}^{p_var1}"
            
        str_var2 = ""
        if p_var2 > 0:
            str_var2 = var2 if p_var2 == 1 else f"{var2}^{p_var2}"
            
        # Junta o coeficiente com as variáveis
        if coeficiente == 1 and (p_var1 > 0 or p_var2 > 0):
            termo_atual = f"{str_var1}{str_var2}"
        else:
            termo_atual = f"{coeficiente}{str_var1}{str_var2}"
            
        termos.append(termo_atual)
        
    # Une todos os termos com o sinal de adição
    expansao = " + ".join(termos)
    return expansao

# --- Teste do Programa ---
if __name__ == "__main__":
    print("--- Gerador de Binômio de Newton ---")
    try:
        expoente = int(input("Digite o valor do expoente (n): "))
        resultado = binomio_newton(expoente)
        
        print(\nf"Resultado para (x + y)^{expoente}:")
        print(resultado)
    except ValueError:
        print("Por favor, digite um número inteiro válido.")