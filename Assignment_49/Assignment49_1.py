import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix,ConfusionMatrixDisplay

def DiabetesClassifier(DataPath):
    border = "="*70

    #################################################################
    # Step 1 : Exploratory Data Analysis(EDA)
    #################################################################

    print(border)
    print("Step 1 : Exploratory Data Analysis(EDA)")
    print(border)

    # Load the dataset
    df = pd.read_csv(DataPath)

    # Display first 5 rows
    print("-"*70)
    print("First 5 rows : ")
    print(df.head())

    # Check column info
    print("-"*70)
    print(df.info())

    # Check for null values
    print("-"*70) 
    print("Null values : ")
    print(df.isnull().sum())

    # Statistics using describe()
    print("-"*70)
    print("Statistical report of dataset : ")
    print(df.describe())

    # Plot the Target distribution
    sns.countplot(x="Outcome", data=df)
    plt.show()

    # Use graph likes hist, boxplot, or pairplot to identify patterns or outliers
    df.hist(figsize=(12,10))
    plt.show()

    plt.figure(figsize=(12,6))
    df.boxplot()
    plt.xticks(rotation=45)
    plt.show()

    sns.pairplot(df, hue="Outcome")
    plt.show()

    #################################################################
    # Step 2 : Data Preprocessing
    #################################################################

    print(border)
    print("Step 2 : Data Preprocessing")
    print(border)

    # Check missing values
    print("-"*70)
    print("Missing values : ")
    print(df.isnull().sum())

    # Handle zero values
    columns = ["Glucose","BloodPressure","SkinThickness","Insulin","BMI"]

    for col in columns:
        df[col] = df[col].replace(0, np.nan)
        df[col] = df[col].fillna(df[col].median())

    # Split features and target
    X = df.drop("Outcome", axis=1)
    Y = df["Outcome"]

    # train test split first
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    # Feature scaling
    scalar = StandardScaler()
    X_train = scalar.fit_transform(X_train)
    X_test = scalar.transform(X_test)

    #################################################################
    # Step 3 : Model Building
    #################################################################

    print(border)
    print("Step 3 : Model Building")
    print(border)

    # Create base models
    model_lr = LogisticRegression(max_iter=5000)
    model_dt = DecisionTreeClassifier(random_state=42)
    model_knn = KNeighborsClassifier(n_neighbors=5)

    # Train base models
    model_lr.fit(X_train,Y_train)
    model_dt.fit(X_train,Y_train)
    model_knn.fit(X_train,Y_train)

    print("Model trained successfully")

    #################################################################
    # Step 4 : Model Evaluation
    #################################################################

    print(border)
    print("Step 4 : Model Evaluation")
    print(border)

    def evaluate_model(name, model,X_test,Y_test):
        pred = model.predict(X_test)

        print("-"*70)
        print("Model:", name)
        print("-"*70)

        # Accuracy 
        accuracy = accuracy_score(Y_test,pred)
        print("-"*70)
        print("Accuracy : ",accuracy)

        # Classification report
        print("-"*70)
        print("Classification report : \n",classification_report(Y_test,pred))

        # Confusion matrix
        cm = confusion_matrix(Y_test,pred)
        print("-"*70)
        print("Confusion matrix : \n",cm)

        # Visualization
        disp = ConfusionMatrixDisplay(confusion_matrix=cm)
        disp.plot()
        plt.title(f"Confusion Matrix - {name}")
        plt.show()

    # Evaluate all models
    evaluate_model("Logistic Regression", model_lr, X_test, Y_test)
    evaluate_model("Decision Tree", model_dt, X_test, Y_test)
    evaluate_model("KNN", model_knn, X_test, Y_test)

    #################################################################
    # Step 5 : Final output
    #################################################################

    print(border)
    print("Step 5 : Final output")
    print(border)

    # Take sample patient form dataset 
    new_patient = X.iloc[[0]]

    # Scale the data
    new_patient_scaled = scalar.transform(new_patient)

    # Predict using Logistic Regression 
    prediction = model_lr.predict(new_patient_scaled)

    # Display patient data
    print("-"*70)
    print("Patient data: ")
    print(new_patient)

    # Display  prediction
    print("-"*70)
    if prediction[0] == 1:
        print("Prediction : Patient is Diabetic")
    else:
        print("Prediction : Patient is not diabetic")

    # Save the prediction into CSV
    result_df = new_patient.copy()

    result_df["Prediction"] = ["Diabetic" if prediction[0] == 1 else "Not Diabetic"]

    result_df.to_csv("Diabetes_Prediction_csv", index=False)

    print("-"*70)
    print("Prediction saved successfully into Diabetes_Prediction_csv")
    print("-"*70)

def main():
    DiabetesClassifier("diabetes.csv")

if __name__ == "__main__":
    main()