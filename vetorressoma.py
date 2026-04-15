def somar_vetores(v1, v2):
    # Verifica se os vetores têm o mesmo tamanho para que a soma seja possível
    if len(v1) != len(v2):
        raise ValueError("Os vetores precisam ter o mesmo número de elementos.")
    
    # Soma os elementos de mesma posição (índice)
    vetor_soma = [v1[i] + v2[i] for i in range(len(v1))]
    return vetor_soma

# Exemplo de uso

vetor_a = [1, 5, 9]