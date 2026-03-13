import numpy as np

class Perceptron:
    def __init__(self, learning_rate=0.1, n_iterations=100):
        self.lr = learning_rate
        self.n_iter = n_iterations
        self.weights = None
        self.bias = None

    def activation_function(self, x):
        # Função de Degrau: retorna 1 se x >= 0, caso contrário 0
        return 1 if x >= 0 else 0

    def fit(self, X, y):
        n_samples, n_features = X.shape
        # Inicializa pesos com zero
        self.weights = np.zeros(n_features)
        self.bias = 0