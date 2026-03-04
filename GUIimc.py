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
        
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# Configuração da Janela Principal
janela = tk.Tk()
janela.title("Calculadora de IMC")
janela.geometry("300x350")
janela.configure(padx=20, pady=20)

# Interface
tk.Label(janela, text="Peso (kg):", font=("Arial", 10)).pack(pady=5)
entry_peso = tk.Entry(janela, font=("Arial", 12), justify='center')
entry_peso.pack(pady=5)

tk.Label(janela, text="Altura (ex: 1.75):", font=("Arial", 10)).pack(pady=5)
entry_altura = tk.Entry(janela, font=("Arial", 12), justify='center')
entry_altura.pack(pady=5)

btn_calcular = tk.Button(janela, text="Calcular IMC", command=calcular_imc, 
                         bg="#3498db", fg="white", font=("Arial", 10, "bold"), pady=5)
btn_calcular.pack(pady=20, fill='x')

resultado_label = tk.Label(janela, text="", font=("Arial", 12, "bold"))
resultado_label.pack(pady=10)

janela.mainloop()