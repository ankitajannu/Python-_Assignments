import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,confusion_matrix, ConfusionMatrixDisplay
from sklearn.tree import plot_tree

##################################################################
# Function : MarvellousClassifier
# Description : Complete Machine Learining workflow using 
#               DecisionTreeClassifier
##################################################################

def MarvellousClassifier(DataPath):
    border = "="*70

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

    print("-"*70)
    print("Input columns : ",X.columns.tolist())
    print("Output column : FinalResult")

    # Split dataset
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,random_state=42, test_size=0.2)

    print("-"*70)
    print("Information of training and testing data")
    print("X_train shape : ",X_train.shape)
    print("X_test shape : ",X_test.shape)
    print("Y_train shape : ",Y_train.shape)
    print("Y_test shape : ",Y_test.shape)
    print("-"*70)

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
    # Step 6 : Decision Tree Visualization
    ##################################################################

    print(border)
    print("Step 6 : Decision Tree Visualization")
    print(border)

    # Plot Decision Tree
    plt.figure(figsize=(18,10))

    plot_tree(
        model,
        feature_names=X.columns,
        class_names=["FAIL","PASS"],
        filled=True
    )

    plt.title("Decision Tree Visualization")
    plt.show()

    ##################################################################
    # Identify Root node feature
    ##################################################################

    # Root node feature index
    root_index = model.tree_.feature[0]

    # Root feature name
    root_feature = X.columns[root_index]

    print("Feature at root node : ",root_feature)

    print("-"*70)

    ##################################################################
    # Explanation
    ##################################################################

    print("Why was this feature selected first ?")

    print("\nThe root node is selected based on the feature")
    print("that gives the best splitof the dataset")

    print("\nDecision Tree choosesthe feature with : ")
    print("1.Highest Information Gain OR")
    print("2.Lowest Gini Impurity")

    print("\nThis means the selected feature separates : ")
    print("PASS and FAIL students more effectively")
    print("than the other features")

    print("\nHence,",root_feature,"was selected first because")
    print("it has the strongest influence on predicting FinalResult")

    print("-"*70)

    print("Obesrvation : ")
    print(root_feature,"provides the most useful decision-making")
    print("information for classifying students")

    ##################################################################
    # Step 7 : Feature importnace analysis
    ##################################################################

    print(border)
    print("Step 7 : Feature importnace analysis")
    print(border)

    # Get feature importance scores
    importance = model.feature_importances_

    # Display feature importance 
    print("Feature importance scores : ")

    for feature, score in zip(X.columns,importance):
        print(feature," : ",round(score,4))

    # Find most important feature
    max_index = np.argmax(importance)
    most_importance = X.columns[max_index]

    # Find least importance feature
    min_index = np.argmin(importance)
    least_important = X.columns[min_index]

    print("-"*70)

    print("Most important feature : ",most_importance)
    print("Least important feature : ",least_important)

    print("-"*70)

    print("Observation : ")
    print(most_importance,"contributes the most in FinalResult")
    print(least_important,"contributes the least in FinalResult")

    ##################################################################
    # Step 8 : Evaluate the model
    ##################################################################

    print(border)
    print("Step 8 : Evaluate the model")
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
    # Step 9 : Accuracy Calculation
    ##################################################################

    print(border)
    print("Step 9 : Accuracy Calculation")
    print(border)

    # Create model accuracy
    accuracy = accuracy_score(Y_test, Y_pred)
    print("Accuracy of model is :  {:.2f}%".format(accuracy*100))

    ##################################################################
    # Step 10 : Manual Accuracy Calculation
    ##################################################################

    print(border)
    print("Step 10 : Manual Accuracy Calculation")
    print(border)

    correct = 0

    for actual,prediction in zip(Y_test,Y_pred):
        if actual == prediction:
            correct = correct + 1

    # Total prediction
    total = len(Y_test)

    # Manual accuracy formula
    manual_accuracy = correct / total

    print("Correct prediction : ",correct)
    print("Total prediction : ",total)
    print("Manual Accuracy : {:.2f}%".format(manual_accuracy * 100))
    print("Sklearn Accuracy : {:.2f}%".format(accuracy * 100))

    print("-"*70)

    # Verify both accuracies
    if round(manual_accuracy,4) == round(accuracy,4):
        print("Verification successful : Both accuracies  match")
    else:
        print("Verification Failed : Accuracies do not match")

    ##################################################################
    # Step 11 : Identified Misclassified Students
    ##################################################################

    print(border)
    print("Step 11 : Identified Misclassified Students")
    print(border)

    # Compare actual and predicted values
    misclassified = Y_test != Y_pred

    # Get indexes of misclassified students
    misclassified_indexes = Y_test[misclassified].index

    # Display misclassified rows
    misclassified_students = df.loc[misclassified_indexes]

    print("Misclassified students : ")
    print(misclassified_students)

    print(border)

    # Count misclassified students
    total_misclassified = len(misclassified_students)

    print("Total Misclassifed students : ",total_misclassified)

    print(border)

    print("Actual vs Predicted values : ")
     
    for actual,predicted in zip(Y_test[misclassified],Y_pred[misclassified]):
        print("Actual : ",actual," Predicted : ",predicted)
    
    print(border)

    print("Observation : ")
    print("1.Misclassified students usually have average or borderline performance")
    print("2.Their features may contain mixed indicators of PASS and FAIL")
    print("3.Decision Tree may get confused when values are close to decision boundaries")

    ##################################################################
    # Step 12 : Confusion Matrix Generation
    ##################################################################

    print(border)
    print("Step 12 : Confusion Matrix Generation")
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

    print("-"*70)
    print("Explanation of Confusion Matrix")
    print("-"*70)

    print("True Positive (TP)  : Model predicted PASS and student actually PASSED")
    print("True Negative (TN)  : Model predicted FAIL and student actually FAILED")
    print("False Positive (FP) : Model predicted PASS but student actually FAILED")
    print("False Negative (FN) : Model predicted FAIL but student actually PASSED")

    ##################################################################
    # Step 13 : Training and Testing accuracy 
    ##################################################################

    print(border)
    print("Step 13 : Training and Testing Accuracy")
    print(border)

    # Training Accuracy
    train_accuracy = model.score(X_train, Y_train)

    # Testing Accuracy
    test_accuracy = model.score(X_test, Y_test)

    print("Training Accuracy : {:.2f}%".format(train_accuracy * 100))
    print("Testing Accuracy  : {:.2f}%".format(test_accuracy * 100))

    ##################################################################
    # Step 13.1 : Overfitting / Underfitting Check
    ##################################################################

    print(border)
    print("Step 13.1 : Model Analysis")
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
    # Step 14 : Remove SleepHours features and Retrain model
    ##################################################################

    print(border)
    print("Step 14 : Remove SleepHours features and Retrain model")
    print(border)

    X_new = df.drop(columns=['FinalResult','SleepHours'])

    # Output feature
    Y_new = df['FinalResult']

    print("Updated Input columns : ")
    print(X_new.columns.tolist())

    # Split dataset again
    X_train_new, X_test_new, Y_train_new, Y_test_new = train_test_split(X_new,Y_new,random_state=42, test_size=0.2)

    # Create new model
    new_model = DecisionTreeClassifier(
        criterion="gini",
        max_depth=5,
        random_state=42
    )

    # Train model
    new_model.fit(X_train_new,Y_train_new)

    # Test model
    Y_pred_new = new_model.predict(X_test_new)

    # Calculate new accuracy
    new_accuracy = accuracy_score(Y_test_new,Y_pred_new)

    print("Previous Accuracy : {:.2f}%".format(accuracy * 100))
    print("New Accuracy      : {:.2f}%".format(new_accuracy * 100))

    print("-"*70)

    # Compare performace

    if new_accuracy > accuracy:
        print("Obesrvation : Removing SleepHours improved the model performance.")
    elif new_accuracy < accuracy:
        print("Obesrvation : Removing SleepHours reduced the model performance.")
    else:
        print("Obesrvation : Removing SleepHours did not affect the model performance.")

    ##################################################################
    # Step 15 : Training model only using studyHours and Attendance
    ##################################################################

    print(border)
    print("Step 15 : Training model only using studyHours and Attendance")
    print(border)


    # Select one two features
    X_small = df[['StudyHours','Attendance']]

    # Output feature
    Y_small = df['FinalResult']

    print("Selected Features  : ")
    print(X_small.columns.tolist())

    # Split dataset again
    X_train_small, X_test_small, Y_train_small, Y_test_small = train_test_split(X_small,Y_small,random_state=42, test_size=0.2)

    # Create new model
    small_model = DecisionTreeClassifier(
        criterion="gini",
        max_depth=5,
        random_state=42
    )

    # Train model
    small_model.fit(X_train_small,Y_train_small)

    # Test model
    Y_pred_small = small_model.predict(X_test_small)

    # Calculate  accuracy
    small_accuracy = accuracy_score(Y_test_small,Y_pred_small)

    print("Previous Accuracy : {:.2f}%".format(accuracy * 100))
    print("New Accuracy      : {:.2f}%".format(small_accuracy * 100))

    print("-"*70)

    # Compare performace

    if small_accuracy >= accuracy:
        print("Obesrvation : Model is still performing very well using only two features.")
    elif small_accuracy >= 0.70:
        print("Obesrvation : Model performing is acceptable with only  two features.")
    else:
        print("Obesrvation : Model performance decreased significantly after reducing features.")

    ##################################################################
    # Step 16 : Comparing different max_depth values
    ##################################################################

    print(border)
    print("Step 16 : Comparing different max_depth values")
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
        print("-"*70)

    print("Observation : ")

    print("1. Small max_depth may cause underfitting.")
    print("2. Large max_depth may cause overfitting.")
    print("3. Moderate depth usually gives balanced performance.")

    ##################################################################
    # Step 17 : Comparing different random_state values
    ##################################################################

    print(border)
    print("Step 17 : Comparing different max_depth values")
    print(border)

    states = [0,10,42]

    for state in states:

        # Split dataset using current random_state
        X_train_rs, X_test_rs, Y_train_rs, Y_test_rs = train_test_split(
            X,
            Y,
            test_size=0.2,
            random_state=state
        )

        # Create model
        rs_model = DecisionTreeClassifier(
            criterion="gini",
            max_depth=5,
            random_state=state
        )

        # Train maodel
        rs_model.fit(X_train_rs, Y_train_rs)

        # Predict output
        rs_pred = rs_model.predict(X_test_rs)

        # Calculate accuracy
        rs_accuracy = accuracy_score(Y_test_rs, rs_pred)

        print("random_state =", state)
        print("Testing Accuracy : {:.2f}%".format(rs_accuracy * 100))
        print("-"*70)

    print("Observation : ")

    print("1. Different random_state values create different train-test splits.")
    print("2. Testing accuracy may change slightly depending on data distribution.")
    print("3. If accuracy changes a lot, model performance may not be stable.")
    print("4.Similar accuracies indicates that the model is stable and reliable.")

    ##################################################################
    # Step 18 : Predict Result for New Student
    ##################################################################

    print(border)
    print("Step 18 : Predict Result for New Student")
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
    # Step 19 : Predict Result for 5 New Student
    ##################################################################

    print(border)
    print("Step 19 : Predict Result for 5  New Student")
    print(border)

    # New Student data
    new_students = pd.DataFrame({
        'StudyHours' : [6, 2, 8, 4, 7],
        'Attendance' : [85, 60, 92, 70, 88],
        'PreviousScore' : [75, 40, 90, 55, 80],
        'AssignmentsCompleted' : [8, 3, 10, 5, 9],
        'SleepHours' : [7, 5, 8, 6, 7]
    })

    print("New students data : ")
    print(new_students)

    # Predict results
    predictions = model.predict(new_students)

    print("-"*70)
    print("Prediction results : ")
    print("-"*70)

    # Display prediction clearly
    for i in range(len(predictions)):
        print("Student",i+1)

        print("StudyHours : ",new_students.iloc[i]['StudyHours'])
        print("Attendance : ",new_students.iloc[i]['Attendance'])
        print("PreviousScore : ",new_students.iloc[i]['PreviousScore'])
        print("AssignmentsCompleted : ",new_students.iloc[i]['AssignmentsCompleted'])
        print("SleepHours : ",new_students.iloc[i]['SleepHours'])

        if predictions[i] == 1:
            print("Predicted result : PASS")
        else:
            print("Predicted result : FAIL")

        print("-"*70)

    ##################################################################
    # Step 20 : Add Performance Feature
    ##################################################################

    print(border)
    print("Step 20 : Add Performance Feature")
    print(border)

    # Create new feature
    df['PerformanceIndex'] = (df['StudyHours'] * 2) + df['Attendance']

    print("New column added successfully")
    print("PerformanceIndex = (StudyHours * 2) + Attendance")

    print("-"*70)

    # Select one two features
    X_new_feature = df.drop(columns=['FinalResult'])

    # Output feature
    Y_new_feature = df['FinalResult']

    # Split dataset again
    X_train_pf, X_test_pf, Y_train_pf, Y_test_pf = train_test_split(X_new_feature,Y_new_feature,random_state=42, test_size=0.2)

    # Create new model
    pf_model = DecisionTreeClassifier(
        criterion="gini",
        max_depth=5,
        random_state=42
    )

    # Train model
    pf_model.fit(X_train_pf,Y_train_pf)

    # Test model
    Y_pred_pf = pf_model.predict(X_test_pf)

    # Calculate  accuracy
    pf_accuracy = accuracy_score(Y_test_pf,Y_pred_pf)

    print("Previous Accuracy : {:.2f}%".format(accuracy * 100))
    print("New Accuracy      : {:.2f}%".format(pf_accuracy * 100))

    print("-"*70)

    # Compare performace

    if pf_accuracy > accuracy:
        print("Observation : Accuracy improved after adding PerformanceIndex.")
        print("The new feature helps the model understand student performance better.")
    elif pf_accuracy < accuracy:
        print("Observation : Accuracy decreased after adding PerformanceIndex.")
        print("The new feature may not be contributing useful information.")
    else:
        print("Observation : Accuracy remained the same.")
        print("The new feature did not significantly affect model performance.")

     ##################################################################
    # Step 21 : Train model with max_depth = None
    ##################################################################

    print(border)
    print("Step 21 : Train model with max_depth = None")
    print(border)

    # Create model
    deep_model = DecisionTreeClassifier(
        criterion="gini",
        max_depth=None,
        random_state=42
    )

    # Train maodel
    deep_model.fit(X_train, Y_train)

    # Predict output
    deep_pred = deep_model.predict(X_test)

    ##################################################################
    # Calculate Training and Testing Accuracy
    ##################################################################

    # Training accuracy
    deep_train_accuracy = deep_model.score(X_train, Y_train)

    # Testing accuracy
    deep_test_accuracy = deep_model.score(X_test, Y_test)

    print("Training Accuracy : {:.2f}%".format(deep_train_accuracy * 100))
    print("Testing Accuracy  : {:.2f}%".format(deep_test_accuracy * 100))

    print("-"*70)

    if deep_train_accuracy == 1.0 and deep_test_accuracy < deep_train_accuracy:
        print("Observation : ")
        print("Training accuracy is 100% but testing accuracy is lower")

        print("\nThis happens because of OVERFITTING")

        print("\nExplaination : ")

        print("1.max_depth = None allows the tree to grow completely")
        print("2.The model memorizes the training dataset")
        print("3.It learns noise and unnecessary patterns")
        print("4.Therefore, it performs perfectly on training data")
        print("5.but it fails to generalize well on unseen test data")

    else:
        print("Observation :")
        print("Model is not severely overfitting.")

    ##################################################################
    # Step 22 : Final Conclusion
    ##################################################################

    print(border)
    print("Step 22 : Final Conclusion")
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
    border = "="*70

    print(border)
    print("Student Performance using DecisionTreeClassifier")
    print(border)

    MarvellousClassifier("student_performance_ml.csv")

##################################################################
# Starter
##################################################################

if __name__ == "__main__":
    main()