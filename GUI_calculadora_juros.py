import tkinter as tk
from tkinter import ttk, messagebox

def calcular():
    """Lê os valores, faz o cálculo e atualiza a interface."""
    try:
        # Pega os valores digitados e troca vírgula por ponto (padrão brasileiro)
        porcentagem = float(entry_porcentagem.get().replace(',', '.'))
        valor = float(entry_valor.get().replace(',', '.'))
        
        # Faz o cálculo matemático
        resultado = (porcentagem / 100) * valor
        
        # Exibe o resultado formatado com 2 casas decimais
        label_resultado.config(text=f"Resultado: {resultado:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))
        
    except ValueError:
        # Mostra um alerta se o usuário não digitar um número válido
        messagebox.showerror("Erro de Digitação", "Por favor, insira apenas números válidos.")