import matplotlib.pyplot as plt

def buscar_primeiros_n_primos(n):
    primos = []
    numero_atual = 2
    while len(primos) < n:
        # Verifica se o número_atual é divisível por algum número anterior
        for i in range(2, int(numero_atual**0.5) + 1):
            if (numero_atual % i) == 0:
                break
        else:
            primos.append(numero_atual)
        numero_atual += 1
    return primos

# Quantidade de primos desejada
n = 17
lista_primos = buscar_primeiros_n_primos(n)
posicoes = list(range(1, n + 1))