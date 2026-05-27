import math

def eh_primo(n):
    """Verifica se um número inteiro n é primo."""
    # Números menores ou iguais a 1 não são primos
    if n <= 1:
        return False
    # 2 e 3 são primos
    if n <= 3:
        return True
    # Elimina múltiplos de 2 e 3 rapidamente
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Testa divisores de 5 até a raiz quadrada de n
    # Números primos da forma 6k +/- 1
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
            
    return True