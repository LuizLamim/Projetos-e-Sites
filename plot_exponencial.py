import numpy as np
import matplotlib.pyplot as plt

def plotar_exponencial():
    """
    Cria um gráfico de uma função exponencial y = a^x, 
    onde 'a' é a base escolhida pelo usuário.
    """
    print("--- Plotter de Equação Exponencial (y = a^x) ---")
    
    try:
        # Solicita a base da função ao usuário
        # Em funções exponenciais, a base 'a' deve ser positiva e diferente de 1
        a = float(input("Digite o valor da base (a): "))
        
        if a <= 0:
            print("\nErro: A base 'a' deve ser maior que zero.")
            return
        if a == 1:
            print("\nNota: Com base 1, a função é uma linha constante (y = 1).")
        
        # Define o intervalo de x (de -2 a 5 para uma boa visualização)
        x = np.linspace(-2, 5, 400)
        
        # Calcula os valores de y
        y = a ** x
        
        # Configuração do gráfico
        plt.figure(figsize=(10, 6))
        plt.plot(x, y, label=f'$y = {a}^x$', color='blue', linewidth=3)
        
        # Elementos visuais e estilização
        plt.title(f'Gráfico da Função Exponencial $y = {a}^x$', fontsize=14)
        plt.xlabel('x')
        plt.ylabel('y')
        
        # Adiciona linhas dos eixos x e y
        plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
        plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
        
        # Grade e legenda
        plt.grid(True, linestyle=':', alpha=0.6)
        plt.legend()
        
        # Limites do eixo y para evitar que o gráfico fique muito "esticado" verticalmente
        if a > 1:
            plt.ylim(-0.5, max(y) * 1.1)
        else:
            plt.ylim(-0.5, max(1.5, max(y) * 1.1))

        print("\nGerando gráfico...")
        plt.show()
        
    except ValueError:
        print("\nErro: Por favor, insira um número válido para a base.")
    except Exception as e:
        print(f"\nOcorreu um erro inesperado: {e}")

if __name__ == "__main__":
    plotar_exponencial()
