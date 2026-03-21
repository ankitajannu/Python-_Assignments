import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.preprocessing import MinMaxScaler

def main():
    X = [1,2,3,4,5]
    Y = [20000,25000,30000,35000,40000]

    print("Values of independent variable X - ",X)
    print("Values of dependent variable Y - ",Y)

    Y = np.array(Y).reshape(-1,1)

    scaler = MinMaxScaler()
    Y_Scaled = scaler.fit_transform(Y).flatten()

    X_mean = np.mean(X)
    Y_mean = np.mean(Y_Scaled)

    print("Mean of X : ",X_mean)
    print("Mean of Y : ",Y_mean)

    n = len(X)

    numerator = 0
    denominator = 0

    for i in range(n):
        numerator = numerator + ((X[i] - X_mean) * (Y_Scaled[i] - Y_mean))
        denominator = denominator + ((X[i] - X_mean) ** 2)

    m = numerator / denominator

    print("Slope of line (m) : ",m)

    c = Y_mean - (m * X_mean)

    print("Intercept of line (c) : ",c)

    x = np.linspace(1,6,n)
    y = c + m * x

    Y_predicted = 0

    for i in range(n):
        X = np.linspace(1,6,n)
        Y_predicted = m * X + c

    print("Y_predicted is : ",Y_predicted)

    MSE = 0

    MSE = mean_squared_error(Y_Scaled,Y_predicted)
    print("MSE : ",MSE)

    r2 = r2_score(Y_Scaled,Y_predicted)
    print("R square values : ",r2)

    plt.plot(x,y,color = 'g',label = "Regression line")
    plt.scatter(X,Y_Scaled,color = 'r',label = "Data points")
    plt.scatter(X,Y_predicted,color = 'b',label = "Predicted points")

    plt.xlabel("X : Independent variables")
    plt.ylabel("Y : Dependent variables")

    plt.legend()
    plt.show()

    # -------------------------------
    # Predict salary for 6 years
    # -------------------------------

    new_X = 6

    Y_new_scaled = m * new_X + c
    print("Scaled prediction for 6 years :", Y_new_scaled)

    Y_new_actual = scaler.inverse_transform([[Y_new_scaled]])

    print("Predicted salary for 6 years experience :", Y_new_actual[0][0])

if __name__ == "__main__":
    main()