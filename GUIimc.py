import tkinter as tk
from tkinter import messagebox

def calcular_imc():
    try:
        # Pega os valores das caixas de entrada
        peso = float(entry_peso.get().replace(',', '.'))
        altura = float(entry_altura.get().replace(',', '.'))
        
        # Cálculo do IMC
        imc = peso / (altura ** 2)
        
        # Determina a categoria
        if imc < 18.5:
            categoria = "Abaixo do peso"
        elif 18.5 <= imc < 25:
            categoria = "Peso normal"
        elif 25 <= imc < 30:
            categoria = "Sobrepeso"
        else:
            categoria = "Obesidade"
            
        # Exibe o resultado formatado
        resultado_label.config(text=f"IMC: {imc:.2f}\nStatus: {categoria}", fg="#2c3e50")