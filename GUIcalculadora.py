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

        # Criação e posicionamento dos botões
        for (texto, linha, col) in botoes:
            if texto == '=':
                btn = tk.Button(self.root, text=texto, padx=20, pady=20, font=('Arial', 14, 'bold'),
                                command=self.calcular, bg="#4CAF50", fg="white")
            elif texto == 'C':
                btn = tk.Button(self.root, text=texto, padx=20, pady=20, font=('Arial', 14, 'bold'),
                                command=self.limpar, bg="#f44336", fg="white")
            else:
                btn = tk.Button(self.root, text=texto, padx=20, pady=20, font=('Arial', 14),
                                command=lambda t=texto: self.adicionar_valor(t))
            
            # Ajuste de layout (Grid)
            btn.grid(row=linha, column=col, sticky="nsew", padx=2, pady=2)

        # Configurar as linhas e colunas para expandirem uniformemente
        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)

    def adicionar_valor(self, valor):
        """Adiciona números ou operadores ao visor"""
        self.expressao += str(valor)
        self.texto_entrada.set(self.expressao)

    def limpar(self):
        """Limpa o visor"""
        self.expressao = ""
        self.texto_entrada.set("")

    def calcular(self):
        """Realiza o cálculo matemático"""
        try:
            # A função eval analisa a string matemática e executa o cálculo
            resultado = str(eval(self.expressao))
            self.texto_entrada.set(resultado)
            self.expressao = resultado # Atualiza para permitir cálculos contínuos
        except ZeroDivisionError:
            self.texto_entrada.set("Erro")
            self.expressao = ""
        except SyntaxError:
            self.texto_entrada.set("Erro")
            self.expressao = ""
        except Exception as e:
            self.texto_entrada.set("Erro")
            print(f"Erro detalhado: {e}")

# Execução do programa
if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()