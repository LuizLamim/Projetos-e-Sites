def calcular_coeficiente_angular():
    print("--- Calculadora de Coeficiente Angular ---")
    print("Insira as coordenadas do Ponto 1 (x1, y1):")

    try:
        x1 = float(input("x1: "))
        y1 = float(input("y1: "))
        
        print("\nInsira as coordenadas do Ponto 2 (x2, y2):")
        x2 = float(input("x2: "))
        y2 = float(input("y2: "))
        
        # Cálculo das variações (Deltas)
        delta_y = y2 - y1
        delta_x = x2 - x1