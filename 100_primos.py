def eh_primo(n):
    """Retorna True se o número for primo, e False caso contrário."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        return True
    
# Lista para armazenar os números primos encontrados
numeros_primos = []
numero_atual = 2

# Loop continua até a lista ter 100 elementos
while len(numeros_primos) < 500:
    if eh_primo(numero_atual):
        numeros_primos.append(numero_atual)
    numero_atual += 1

# Exibe o resultado formatado
print("Os 1000 primeiros números primos são:")
for idx, primo in enumerate(numeros_primos, 1):
    print(f"{idx}º: {primo}")