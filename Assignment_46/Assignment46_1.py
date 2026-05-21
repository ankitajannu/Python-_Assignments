from sklearn.linear_model import LinearRegression

def RegressionModel():
    X = [[1],[2],[3],[4],[5]]
    Y = [50,55,60,65,70]

    model = LinearRegression()

    model.fit(X,Y)

    print("Coefficient is : ",model.coef_[0])

    print("Intercept is : ",model.intercept_)

def main():
    RegressionModel()

if __name__ == "__main__":
    main()