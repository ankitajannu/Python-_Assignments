import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,confusion_matrix, ConfusionMatrixDisplay

##################################################################
# Function : MarvellousClassifier
# Description : Complete Machine Learining workflow using 
#               DecisionTreeClassifier
##################################################################

def MarvellousClassifier(DataPath):
    border = "-"*70

    ##################################################################
    # Step 1 : Load the Dataset
    ##################################################################

    print(border)
    print("Step 1 : Load the Dataset")
    print(border)

    # Read dataset from CSV file
    df = pd.read_csv(DataPath)

    print("Datasets gets loaded successfully")

    # Display first 5 records
    print("Initial enteries from dataset : ")
    print(df.head())

    ##################################################################
    # Step 2 : Data Analysis
    ##################################################################

    print(border)
    print("Step 2 : Data Analysis")
    print(border)

    # Shape of dataset
    print("Shape of dataset : ",df.shape)

    # Column names
    print("Column names : ",list(df.columns))

    # Check missing values
    print("Missing values (Per column)")
    print(df.isnull().sum())

    # Statistical report 
    print("Statistical report of dataset")
    print(df.describe())

    ##################################################################
    # Step 3 : Visualization
    ##################################################################

    print(border)
    print("Step 3 : Visualization")
    print(border)

    # Scatter plot of StudyHours vs PreviousScore
    plt.figure(figsize=(7,5))

    for fr in df["FinalResult"].unique():
        temp = df[df["FinalResult"] == fr]
        plt.scatter(temp["StudyHours"], temp["PreviousScore"], label=fr)

    plt.title("Student_Performance : StudyHours vs PreviousScore")
    plt.xlabel("StudyHours")
    plt.ylabel("PreviousScore")
    plt.legend()
    plt.grid(True)
    plt.show()

    ##################################################################
    # Step 4 : Split the dataset for training and testing
    ##################################################################

    print(border)
    print("Step 4 : Split the dataset for training and testing")
    print(border)

    # Input features
    X = df.drop(columns=['FinalResult'])

    # Output features
    Y = df['FinalResult']

    print("Shape of X : ",X.shape)
    print("Shape of Y : ",Y.shape)

    print(border)
    print("Input columns : ",X.columns.tolist())
    print("Output column : FinalResult")

    # Split dataset
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,random_state=42, test_size=0.2)

    print(border)
    print("Information of training and testing data")
    print("X_train shape : ",X_train.shape)
    print("X_test shape : ",X_test.shape)
    print("Y_train shape : ",Y_train.shape)
    print("Y_test shape : ",Y_test.shape)
    print(border)

    ##################################################################
    # Step 5 : Model Training
    ##################################################################

    print(border)
    print("Step 5 : Model Training")
    print(border)

    # Create Decision Tree model
    model = DecisionTreeClassifier(
        criterion="gini",
        max_depth=5,
        random_state=42
    )

    # Train model
    model.fit(X_train, Y_train)

    print("Model Training completed")

    ##################################################################
    # Step 6 : Evaluate the model
    ##################################################################

    print(border)
    print("Step 6 : Evaluate the model")
    print(border)

    # Predict output for test data
    Y_pred = model.predict(X_test)

    print("Model Evaluation (testing) completed")

    print(Y_pred.shape)
    
    print("Actual values : ")
    print(Y_test)

    print("Predicted values : " )
    print(Y_pred)

    ##################################################################
    # Step 7 : Accuracy Calculation
    ##################################################################

    print(border)
    print("Step 7 : Accuracy Calculation")
    print(border)

    # Create model accuracy
    accuracy = accuracy_score(Y_test, Y_pred)
    print("Accuracy of model is :  {:.2f}%".format(accuracy*100))

    ##################################################################
    # Step 8 : Confusion Matrix Generation
    ##################################################################

    print(border)
    print("Step 8 : Confusion Matrix Generation")
    print(border)

    # Generate Confusion matrix
    cm = confusion_matrix(Y_test,Y_pred)
    print("Confusion matrix : ")
    print(cm)

    # Display confusion matrix graphically 
    data = ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=model.classes_)
    data.plot()

    plt.title("Confusion matrix of student_performance dataset")
    plt.show()

    print(border)
    print("Explanation of Confusion Matrix")
    print(border)

    print("True Positive (TP)  : Model predicted PASS and student actually PASSED")
    print("True Negative (TN)  : Model predicted FAIL and student actually FAILED")
    print("False Positive (FP) : Model predicted PASS but student actually FAILED")
    print("False Negative (FN) : Model predicted FAIL but student actually PASSED")

    ##################################################################
    # Step 9 : Training and Testing accuracy 
    ##################################################################

    print(border)
    print("Step 9 : Training and Testing Accuracy")
    print(border)

    # Training Accuracy
    train_accuracy = model.score(X_train, Y_train)

    # Testing Accuracy
    test_accuracy = model.score(X_test, Y_test)

    print("Training Accuracy : {:.2f}%".format(train_accuracy * 100))
    print("Testing Accuracy  : {:.2f}%".format(test_accuracy * 100))

    ##################################################################
    # Step 9.1 : Overfitting / Underfitting Check
    ##################################################################

    print(border)
    print("Step 9.1 : Model Analysis")
    print(border)

    difference = abs(train_accuracy - test_accuracy)

    print("Difference between training and testing accuracy : ", difference)

    # Compare accuracies
    if difference < 0.05:
        print("\nModel is well balanced.")

    elif train_accuracy > test_accuracy:
        print("\nModel may be Overfitting.")

    else:
        print("\nModel may be Underfitting.")

    ##################################################################
    # Step 10 : Comparing different max_depth values
    ##################################################################

    print(border)
    print("Step 10 : Comparing different max_depth values")
    print(border)

    depths = [1, 3, None]

    for depth in depths:

        # Create model
        temp_model = DecisionTreeClassifier(
            criterion="gini",
            max_depth=depth,
            random_state=42
        )

        # Train maodel
        temp_model.fit(X_train, Y_train)

        # Predict output
        temp_pred = temp_model.predict(X_test)

        # Calculate accuracy
        temp_accuracy = accuracy_score(Y_test, temp_pred)

        print("max_depth =", depth)
        print("Testing Accuracy : {:.2f}%".format(temp_accuracy * 100))
        print(border)

    print("Observation : ")

    print("1. Small max_depth may cause underfitting.")
    print("2. Large max_depth may cause overfitting.")
    print("3. Moderate depth usually gives balanced performance.")

    ##################################################################
    # Step 11 : Predict Result for New Student
    ##################################################################

    print(border)
    print("Step 11 : Predict Result for New Student")
    print(border)

    # New Student data
    new_student = pd.DataFrame({
        'StudyHours': [6],
        'Attendance': [85],
        'PreviousScore': [66],
        'AssignmentsCompleted': [7],
        'SleepHours': [7]
    })

    # Predict results
    new_predict = model.predict(new_student)

    print("Prediction Result : ",new_predict)

    # Display final output
    if new_predict[0] == 1:
        print("The student is PASS")
    else:
        print("The student is FAIL")

    ##################################################################
    # Step 12 : Final Conclusion
    ##################################################################

    print(border)
    print("Step 9 : Final Conclusion")
    print(border)

    print("DecisionTreeClassifier model was trained successfully.")

    print("\nThe model predicts whether a student will")
    print("Pass or Fail based on student performance data.")

    print("\nAccuracy obtained :", accuracy * 100)

    # Comment on model performance
    if accuracy > 0.80:
        print("\nModel performance is very good.")

    elif accuracy > 0.60:
        print("\nModel performance is acceptable.")

    else:
        print("\nModel performance needs improvement.")

##################################################################
# Main Function
##################################################################

def main():
    border = "-"*70

    print(border)
    print("Student Performance using DecisionTreeClassifier")
    print(border)

    MarvellousClassifier("student_performance_ml.csv")

##################################################################
# Starter
##################################################################

if __name__ == "__main__":
    main()