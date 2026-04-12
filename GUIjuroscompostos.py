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