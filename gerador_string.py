import secrets
import string


def gerar_texto_aleatorio(tamanho):
    # Define o pool de caracteres: letras maiúsculas, minúsculas e números
    # Se quiser incluir símbolos, adicione `+ string.punctuation`
    caracteres = string.ascii_letters + string.digits

    # Gera o texto aleatório com o tamanho escolhido
    texto = "".join(secrets.choice(caracteres) for _ in range(tamanho))
    return texto


# Programa principal
try:
    qtd = int(input("Digite a quantidade de caracteres desejada: "))

    if qtd <= 0:
        print("Por favor, insira um número maior que zero.")
    else:
        resultado = gerar_texto_aleatorio(qtd)
        print("\n--- Texto Gerado ---")
        print(resultado)
        print("--------------------")

except ValueError:
    print("Erro: Por favor, digite apenas números inteiros.")