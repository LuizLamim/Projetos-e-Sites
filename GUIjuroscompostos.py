import tkinter as tk
from tkinter import messagebox

def calcular_juros():
    """Função para calcular os juros e atualizar a interface."""
    try:
        # Coletando e formatando os dados inseridos pelo usuário
        capital = float(entry_capital.get().replace(',', '.'))
        taxa_percentual = float(entry_taxa.get().replace(',', '.'))
        tempo = float(entry_tempo.get())

        # Convertendo a taxa de porcentagem para decimal
        taxa_decimal = taxa_percentual / 100

        # Cálculo de Juros Compostos: M = C * (1 + i)^t
        montante = capital * (1 + taxa_decimal) ** tempo
        juros = montante - capital

        # Formatando o resultado para exibição
        resultado_texto = f"Montante Final: R$ {montante:,.2f}\nJuros Rendidos: R$ {juros:,.2f}"
        
        # Substituindo vírgula por ponto para o padrão brasileiro (opcional)
        resultado_texto = resultado_texto.replace(',', '_').replace('.', ',').replace('_', '.')
        
        label_resultado.config(text=resultado_texto, fg="green")
        
    except ValueError:
        # Tratamento de erro caso o usuário digite letras ou deixe em branco
        messagebox.showerror("Erro de Entrada", "Por favor, insira apenas números válidos.")

# ==========================================
# Configuração da Janela Principal (GUI)
# ==========================================
janela = tk.Tk()
janela.title("Calculadora de Juros Compostos")
janela.geometry("350x350")
janela.config(padx=20, pady=20)
janela.resizable(False, False)


# --- Elementos da Interface (Widgets) ---

# Título
titulo = tk.Label(janela, text="Juros Compostos", font=("Helvetica", 14, "bold"))
titulo.pack(pady=(0, 15))

# Campo: Capital
tk.Label(janela, text="Capital Inicial (R$):").pack()
entry_capital = tk.Entry(janela, width=25, justify="center")
entry_capital.pack(pady=5)

# Campo: Taxa de Juros
tk.Label(janela, text="Taxa de Juros por período (%):").pack()
entry_taxa = tk.Entry(janela, width=25, justify="center")
entry_taxa.pack(pady=5)

# Campo: Tempo
tk.Label(janela, text="Tempo (meses ou anos):").pack()
entry_tempo = tk.Entry(janela, width=25, justify="center")
entry_tempo.pack(pady=5)

# Botão de Calcular
botao_calcular = tk.Button(janela, text="Calcular", command=calcular_juros, 
                           bg="#0052cc", fg="white", font=("Helvetica", 10, "bold"), 
                           width=15, relief="flat", cursor="hand2")
botao_calcular.pack(pady=20)

# Label para exibir o resultado final
label_resultado = tk.Label(janela, text="", font=("Helvetica", 11, "bold"))
label_resultado.pack()

# Iniciar o loop principal da aplicação
janela.mainloop()