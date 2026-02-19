import tkinter as tk
from tkinter import messagebox

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Python")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        # Variável para armazenar o texto do visor
        self.expressao = ""
        self.texto_entrada = tk.StringVar()

        # Configuração do Visor
        entrada = tk.Entry(self.root, textvariable=self.texto_entrada, font=('Arial', 24), bd=10, insertwidth=2, width=14, borderwidth=4, justify="right")
        entrada.grid(row=0, column=0, columnspan=4)

        # Definição dos Botões
        # Layout: (Texto do botão, Linha, Coluna)

        botoes = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]