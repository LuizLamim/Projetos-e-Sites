import tkinter as tk
from tkinter import messagebox
import math

import tkinter as tk
from tkinter import messagebox
import math

def calcular_log():
    try:
        # Captura o valor digitado pelo usuário e converte para decimal
        valor_texto = entrada_x.get().replace(',', '.')
        x = float(valor_texto)

        # Validação matemática: logaritmos não são definidos para x <= 0
        if x <= 0:
            messagebox.showerror("Erro de Matemática", "O valor deve ser estritamente maior que zero.")
            resultado_var.set("Resultado: Inválido")
            return

        # Calcula o logaritmo na base 10
        y = math.log10(x)

        # Atualiza a interface com o resultado e a prova real
        resultado_var.set(f"log₁₀({x}) = {y:.4f}\n\nProva: 10^{y:.4f} ≈ {x}")

    except ValueError:
        # Captura erro caso o usuário digite letras ou símbolos inválidos
        messagebox.showerror("Erro de Entrada", "Por favor, insira um número válido.")
        resultado_var.set("Resultado: Erro")

# 1. Configuração da Janela Principal
janela = tk.Tk()
janela.title("Calculadora Log₁₀")
janela.geometry("350x300")
janela.configure(bg="#f0f4f8")
janela.resizable(False, False)

# 2. Estilo e Fontes
fonte_titulo = ("Helvetica", 12, "bold")
fonte_normal = ("Helvetica", 11)

# 3. Criação dos Elementos da Interface (Widgets)
titulo_label = tk.Label(janela, text="Digite o valor (x > 0):", font=fonte_titulo, bg="#f0f4f8", fg="#333")
titulo_label.pack(pady=(20, 10))

entrada_x = tk.Entry(janela, font=("Helvetica", 14), justify="center", width=15)
entrada_x.pack(pady=5)

botao_calcular = tk.Button(janela, text="Calcular", font=fonte_normal, bg="#005b96", fg="white", 
                           activebackground="#03396c", activeforeground="white", 
                           cursor="hand2", command=calcular_log)
botao_calcular.pack(pady=20)

resultado_var = tk.StringVar()
resultado_var.set("O resultado aparecerá aqui")

resultado_label = tk.Label(janela, textvariable=resultado_var, font=fonte_normal, bg="#f0f4f8", fg="#03396c", justify="center")
resultado_label.pack(pady=10)

# 4. Iniciar o loop principal da aplicação
janela.mainloop()