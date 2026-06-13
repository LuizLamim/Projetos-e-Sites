import secrets
import string

def gerar_texto_aleatorio(tamanho):
    texto = "".join(secrets.choice(caracteres) for _ in range(tamanho))
    return texto