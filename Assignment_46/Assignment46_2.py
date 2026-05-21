from sklearn.linear_model import LinearRegression

def RegressionModel():
    X = [[1],[2],[3],[4],[5]]
    Y = [50,55,60,65,70]

    model = LinearRegression()

    model.fit(X,Y)

    prediction = model.predict([[6]])

    print("Predicted Marks for 6 Study Hours is : ",prediction[0])

def main():
    RegressionModel()

if __name__ == "__main__":
    main()