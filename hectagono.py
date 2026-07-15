import turtle

def desenhar_hectagono(tamanho):
    # Configuração da tela e da tartaruga
    tela = turtle.Screen()
    tela.title("Desenho de um Hectágono")
    tartaruga = turtle.Turtle()

    # Velocidade máxima para desenhar rápido
    tartaruga.speed(0)

    # Um hectágono possui 100 lados
    lados = 100
    # O ângulo externo de um polígono regular é 360/n
    angulo = 360 / lados