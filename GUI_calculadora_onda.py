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

# --- Configuração da Interface Gráfica (GUI) ---

# Cria a janela principal
janela = tk.Tk()
janela.title("Calculadora de Comprimento de Onda")
janela.geometry("350x250")
janela.eval('tk::PlaceWindow . center') # Centraliza a janela

# Título na janela
titulo = tk.Label(janela, text="Cálculo de Onda", font=("Arial", 14, "bold"))
titulo.pack(pady=10)

# Frame para organizar as entradas de velocidade
frame_velocidade = tk.Frame(janela)
frame_velocidade.pack(pady=5)
tk.Label(frame_velocidade, text="Velocidade (m/s):").pack(side=tk.LEFT)
entry_velocidade = tk.Entry(frame_velocidade, width=15)
entry_velocidade.pack(side=tk.LEFT, padx=5)

# Frame para organizar as entradas de frequência
frame_frequencia = tk.Frame(janela)
frame_frequencia.pack(pady=5)
tk.Label(frame_frequencia, text="Frequência (Hz):  ").pack(side=tk.LEFT)
entry_frequencia = tk.Entry(frame_frequencia, width=15)
entry_frequencia.pack(side=tk.LEFT, padx=5)

# Botão de Calcular
botao_calcular = tk.Button(janela, text="Calcular", command=calcular_comprimento, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
botao_calcular.pack(pady=15)

# Label para mostrar o resultado
label_resultado = tk.Label(janela, text="Comprimento de Onda (λ): ---", font=("Arial", 11))
label_resultado.pack(pady=5)

# Inicia o loop principal da interface gráfica
janela.mainloop()