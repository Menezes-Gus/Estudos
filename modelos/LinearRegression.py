import numpy as np


class LinearRegression:

    def __init__(self, learning_rate=0.001, n_iters=1000):
        self.learning_rate = learning_rate
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        y_hat = np.dot(self.weights, X) + self.bias

        #w = w - a * dw
        #b = b - a * db

        

    def predict(self,X,y):
        # w*X+b

