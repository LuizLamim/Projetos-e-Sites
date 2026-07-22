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

# 1. Configuração da Janela Principal
root = tk.Tk()
root.title("Calculadora de %")
root.geometry("320x220")
root.resizable(False, False) # Impede que a janela seja redimensionada

# 2. Configuração de Estilo (Deixa os botões e textos mais bonitos)
style = ttk.Style()
style.configure("TLabel", font=("Segoe UI", 11))
style.configure("TButton", font=("Segoe UI", 11, "bold"))
style.configure("Title.TLabel", font=("Segoe UI", 14, "bold"))

# 3. Criação do Frame (Contêiner principal)
frame = ttk.Frame(root, padding="20")
frame.pack(fill=tk.BOTH, expand=True)

# 4. Criação dos Elementos (Widgets)
titulo = ttk.Label(frame, text="Descubra a Porcentagem", style="Title.TLabel")
titulo.grid(row=0, column=0, columnspan=2, pady=(0, 15))