def eh_primo(n):
    """Verifica se um número é primo."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def encontrar_primos_gemeos(limite):
    """Encontra todos os pares de primos gêmeos até o limite estipulado."""
    primos_gemeos = []