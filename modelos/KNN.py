import numpy as np
from collections import Counter

class KNN:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def __euclidean_distance(self, x1, x2):
        return np.sqrt(np.sum((x1-x2)**2))

    def predict(self, X):
        return [self.__predict(x) for x in X]
    
    def __predict(self, x_query):
        distances = [self.__euclidean_distance(x_query, x_train) for x_train in self.X_train]

        k_indices = np.argsort(distances)[:self.k]
        k_labels = [self.y_train[i] for i in k_indices]


        return int(Counter(k_labels).most_common()[0][0])