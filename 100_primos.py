def eh_primo(n):
    """Retorna True se o número for primo, e False caso contrário."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        return True