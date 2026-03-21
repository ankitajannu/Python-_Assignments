import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, mean_squared_error

def MarvellousPredictor():
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print("Values of independent variables : X - ",X)
    print("Values of dependent variables : Y - ",Y)

    mean_X = np.mean(X)
    mean_Y = np.mean(Y)

    print("X_MEAN is : ",mean_X)    
    print("Y_MEAN is : ",mean_Y)    

    n = len(X) 

    numerator = 0
    denominator = 0

    for i in range(n):
        x_diff = X[i] - mean_X
        y_diff = Y[i] - mean_Y

        print(f"Step {i+1} : ({X[i]} - {mean_X}) * ({Y[i]} - {mean_Y}) = {x_diff} * {y_diff} = {x_diff*y_diff}")

        numerator = numerator + (x_diff * y_diff)
        denominator = denominator + (x_diff ** 2)

    print("\nnumerator = ",numerator)
    print("denominator = ",denominator)
    m = numerator / denominator

    print("Slope of line ie m : ",m)    

    C = mean_Y - (m * mean_X)

    print("Y intercept of line ie C : ",C)

    print("-----Predicted values-----")

    Y_predicted = []

    for i in range(n):
        Y_pred = m * X[i] + C
        Y_predicted.append(Y_pred)
        print(f"X = {X[i]} -> Y = {Y_pred}")

    print("-----MSE values-----")

    errors = []
    for i in range(n):
        err = (Y[i] - Y_predicted[i])**2
        errors.append(err)
        print(f"({Y[i]} - {Y_predicted[i]})² = {err}")

    mse = sum(errors)/n
    print("\nMSE (manual) =", mse)

    print("MSE (sklearn): ",mean_squared_error(Y,Y_predicted))

    r2 = r2_score(Y,Y_predicted)
    print("R square values : ",r2) 
    

def main():
    MarvellousPredictor()

if __name__ == "__main__":
    main()