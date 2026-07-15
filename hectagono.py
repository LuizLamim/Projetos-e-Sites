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
    
    # Loop para desenhar cada lado
    for _ in range(lados):
        tartaruga.forward(tamanho)
        tartaruga.left(angulo)
        
    # Finalizar
    tela.exitonclick()

# Executar a função com tamanho de lado 5
desenhar_hectagono(5)