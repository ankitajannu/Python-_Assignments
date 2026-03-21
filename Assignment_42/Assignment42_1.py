import numpy as np 
import pandas as pd 

def main():
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print("Values of independent variable X - ",X)
    print("Values of dependent variable Y - ",Y)

    X_mean = np.mean(X)
    Y_mean = np.mean(Y)

    print("Mean of X : ",X_mean)
    print("Mean of Y : ",Y_mean)

    n = len(X)

    numerator = 0
    denominator = 0

    for i in range(n):
        numerator = numerator + ((X[i] - X_mean) * (Y[i] - Y_mean))
        denominator = denominator + ((X[i] - X_mean) ** 2)

    m = numerator / denominator

    print("Slope of line (m) : ",m)

    c = Y_mean - (m * X_mean)

    print("Intercept of line (c) : ",c)

if __name__ == "__main__":
    main()