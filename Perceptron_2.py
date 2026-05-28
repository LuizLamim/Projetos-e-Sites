import numpy as np

class Perceptron:
    def __init__(self, taxa_aprendizado=0.1, epocas=10):
        # A taxa de aprendizado define o tamanho do "passo" a cada ajuste
        self.taxa_aprendizado = taxa_aprendizado
        # Épocas são quantas vezes o algoritmo vai ver todo o conjunto de dados
        self.epocas = epocas
        self.pesos = None
        self.bias = None

    def funcao_ativacao(self, x):
        # Função Degrau (Step): Retorna 1 se x for >= 0, senão retorna 0
        return 1 if x >= 0 else 0

    def prever(self, entradas):
        # Calcula a soma ponderada: (Entradas * Pesos) + Bias
        soma_linear = np.dot(entradas, self.pesos) + self.bias
        # Passa o resultado pela função de ativação
        return self.funcao_ativacao(soma_linear)

    def treinar(self, entradas_treino, rotulos):
        # Inicializa pesos e bias com zeros
        self.pesos = np.zeros(entradas_treino.shape[1])
        self.bias = 0.0

        for epoca in range(self.epocas):
            print(f"--- Época {epoca + 1} ---")
            for entradas, rotulo_real in zip(entradas_treino, rotulos):
                # O perceptron tenta adivinhar o resultado
                previsao = self.prever(entradas)
                
                # Calcula o erro (Real - Previsto)
                erro = rotulo_real - previsao
                
                # Se houve erro, ajusta os pesos e o bias
                if erro != 0:
                    self.pesos += self.taxa_aprendizado * erro * entradas
                    self.bias += self.taxa_aprendizado * erro
                
            print(f"Pesos atuais: {self.pesos} | Bias atual: {self.bias:.2f}")

# ==========================================
# Testando o Perceptron com a porta lógica AND
# ==========================================

# Entradas (x1, x2)
dados_treino = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# Saídas esperadas (rotulos) para a porta AND
saidas_esperadas = np.array([0, 0, 0, 1])

# Cria e treina o modelo
meu_perceptron = Perceptron(taxa_aprendizado=0.1, epocas=6)
meu_perceptron.treinar(dados_treino, saidas_esperadas)

# Testando as previsões após o treinamento
print("\nTestando o modelo treinado:")
for entrada in dados_treino:
    resultado = meu_perceptron.prever(entrada)
    print(f"Entrada: {entrada} -> Previsão: {resultado}")