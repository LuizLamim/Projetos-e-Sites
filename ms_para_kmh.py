def converter_ms_para_kmh(velocidade_ms):
    """Converte velocidade de m/s para km/h."""
    velocidade_kmh = velocidade_ms * 3.6
    return velocidade_kmh

# Interface simples para o usuário
print("--- Conversor de Velocidade ---")

try:
    valor_ms = float(input("Digite a velocidade em m/s: "))
    
    resultado = converter_ms_para_kmh(valor_ms)

    print(f"\nA velocidade de {valor_ms} m/s equivale a {resultado:.2f} km/h.")
except ValueError:
    print("Erro: Por favor, insira um número válido.")