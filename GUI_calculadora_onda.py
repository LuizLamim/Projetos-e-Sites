import tkinter as tk
from tkinter import messagebox

def calcular_comprimento():
    """Calcula o comprimento de onda com base na velocidade e frequência inseridas."""
    try:
        # Obtém os valores digitados pelo usuário e converte para float
        velocidade = float(entry_velocidade.get())
        frequencia = float(entry_frequencia.get())
        
        # Validação para evitar divisão por zero
        if frequencia == 0:
            messagebox.showerror("Erro de Cálculo", "A frequência não pode ser igual a zero.")
            return
            
        # Calcula o comprimento de onda (λ = v / f)
        comprimento_onda = velocidade / frequencia
        
        # Atualiza o texto da label de resultado
        label_resultado.config(text=f"Comprimento de Onda (λ): {comprimento_onda:.4f} metros")
        
    except ValueError:
        # Captura o erro caso o usuário digite letras ou deixe em branco
        messagebox.showerror("Erro de Entrada", "Por favor, insira apenas valores numéricos válidos.")