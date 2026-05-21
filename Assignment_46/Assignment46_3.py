from sklearn.linear_model import LinearRegression

def RegressionModel():
    X = [
        [1,7],
        [2,6],
        [3,7],
        [4,6],
        [5,8]
    ]
    Y = [50,55,60,65,70]

    model = LinearRegression()

    model.fit(X,Y)

    print("Coefficient for StudyHours : ",round(model.coef_[0],2))
    print("Coefficient for SleepHours : ",round(model.coef_[1],2))

    print("Intercept is : ",round(model.intercept_,2))

def main():
    RegressionModel()

if __name__ == "__main__":
    main()