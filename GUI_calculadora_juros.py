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

# Campo: Porcentagem
ttk.Label(frame, text="Qual a porcentagem? (%)").grid(row=1, column=0, sticky="w", pady=5)
entry_porcentagem = ttk.Entry(frame, width=12)
entry_porcentagem.grid(row=1, column=1, pady=5)

# Campo: Valor Total
ttk.Label(frame, text="Do valor total:").grid(row=2, column=0, sticky="w", pady=5)
entry_valor = ttk.Entry(frame, width=12)
entry_valor.grid(row=2, column=1, pady=5)

# Botão de Calcular
btn_calcular = ttk.Button(frame, text="Calcular", command=calcular)
btn_calcular.grid(row=3, column=0, columnspan=2, pady=15, ipadx=10)

# Texto do Resultado
label_resultado = ttk.Label(frame, text="Resultado: ---", font=("Segoe UI", 12, "bold"), foreground="#005a9e")
label_resultado.grid(row=4, column=0, columnspan=2)

# 5. Inicia o loop do aplicativo
root.mainloop()