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

        for _ in np.arange(0,self.n_iters,1):
            y_hat = np.dot(X,self.weights) + self.bias

            
            dw = (2/n_samples) * np.dot(X.T, (y_hat-y))
            db = (2/n_samples) * np.sum((y_hat-y))

            #w = w - lr * dw
            #b = b - lr * db
            self.weights = self.weights - self.learning_rate*dw
            self.bias = self.bias - self.learning_rate*db
        

    def predict(self,X):
        y_hat = np.dot(X,self.weights) + self.bias
        return y_hat
        # w*X+b

