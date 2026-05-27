def eh_par(n):
    """Retorna True se o número for par, False caso contrário."""
    return n % 2 == 0

# Exemplo de uso
try:
    num = int(input("Digite um número inteiro: "))
    
    if eh_par(num):
        print(f"O número {num} é par.")
    else:
        print(f"O número {num} é ímpar.")
except ValueError:
    print("Entrada inválida! Por favor, digite um número inteiro.")