def calcular_raiz_quinta(numero):
    # Elevamos o número à potência de 0.2
    return numero ** 0.2

# Solicitar número:
num = float(input("Digite um número para calcular a raiz quinta: "))
resultado = calcular_raiz_quinta(num)

print(f"A raiz quinta de {num} é {resultado:.4f}")