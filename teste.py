def multiplo_de(numero, multiplo):
     resultado = numero % multiplo == 0
     print(f'{numero} é múltiplo de {multiplo}?', end=' ')
     print(resultado)