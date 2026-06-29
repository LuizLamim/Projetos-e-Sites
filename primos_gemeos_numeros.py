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

    # Começamos do 3, pois o único primo par é 2, e ele não forma gêmeo com ninguém acima de 3.
    for n in range(3, limite - 1, 2):
        if eh_primo(n) and eh_primo(n + 2):
            primos_gemeos.append((n, n + 2))
            
    return primos_gemeos

# --- Execução do Programa ---
if __name__ == "__main__":
    limite_usuario = int(input("Digite o limite máximo para buscar primos gêmeos: "))
    
    resultado = encontrar_primos_gemeos(limite_usuario)
    
    print(f"\nEncontrados {len(resultado)} pares de primos gêmeos até {limite_usuario}:")
    for par in resultado:
        print(f"{par[0]} e {par[1]}")