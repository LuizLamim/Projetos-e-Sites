def obter_primeiros_primos(quantidade):
    primos = []
    numero = 2  # Começamos a verificar a partir do 2, que é o primeiro número primo

    while len(primos) < quantidade:
        eh_primo = True
        
        # Verifica se o número é divisível por algum número anterior a ele
        # Otimização: só precisamos checar até a raiz quadrada do número
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                eh_primo = False
                break  # Não é primo, podemos parar de testar