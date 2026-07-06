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