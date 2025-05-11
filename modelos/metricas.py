import numpy as np

def mse(y_hat, y):
    return float(np.mean((y-y_hat)**2))

def accuracy(y_hat, y):
    return float(np.sum(y_hat==y)/len(y_hat))

def confusion_matrix(y_hat, y):
    TP = TN = FP = FN = 0

    for yt, yp in zip(y, y_hat):
        if yt == 1 and yp == 1:
            TP += 1
        elif yt == 0 and yp == 0:
            TN += 1
        elif yt == 0 and yp == 1:
            FP += 1
        elif yt == 1 and yp == 0:
            FN += 1
            
    print(np.array([[TN, FP],
                    [FN, TP]]))