n1 = float(input("Digite o 1º número: "))
n2 = float(input("Digite o 2º número: "))
n3 = float(input("Digite o 3º número: "))
n4 = float(input("Digite o 4º número: "))
n5 = float(input("Digite o 5º número: "))
n6 = float(input("Digite o 6º número: "))

soma = n1 + n2 + n3 + n4 + n5 

print(f"A soma dos 5 números é: {soma}")

# outra forma de escrever o código

soma = 0

# O loop vai rodar 6 vezes
for i in range(1, 7):
    numero = float(input(f"Digite o {i}º número: "))
    soma += numero  # Isso é o mesmo que: soma = soma + numero

print(f"\nO total da soma é: {soma}")