import numpy as np

class LogisticRegression:

    def __init__(self, learning_rate=0.001, n_iters=1000):
        self.learning_rate = learning_rate
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in np.arange(0, self.n_iters):
            linear_preds = np.dot(X,self.weights) + self.bias
            y_hat = 1/(1 + np.exp(- linear_preds))

            #derivadas da função de log-likelihood em favor de w e b
            dw = (1/n_samples) * np.dot(X.T, (y_hat-y))
            db = (1/n_samples) * np.sum((y_hat-y))

            #w = w - lr * dw
            #b = b - lr * db
            self.weights = self.weights - self.learning_rate*dw
            self.bias = self.bias - self.learning_rate*db
        

    def predict_prob(self,X):
        linear_preds = np.dot(X,self.weights) + self.bias
        y_hat = 1/(1 + np.exp(- linear_preds))
        return y_hat
    
    def predict(self,X, treshold = 0.5):
        y_hat_prob = self.predict_prob(X=X)
        y_hat = [0 if y_hat <= treshold else 1 for y_hat in y_hat_prob]
        return y_hat