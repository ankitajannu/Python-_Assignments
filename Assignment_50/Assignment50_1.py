import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix,ConfusionMatrixDisplay,roc_auc_score,roc_curve

def DiabetesClassifier(DataPath):
    border = "="*70

    #################################################################
    # Step 1 : Load and Explore the dataset
    #################################################################

    print(border)
    print("Step 1 : Load and Explore the dataset")
    print(border)

    # Load the dataset
    df = pd.read_csv(DataPath, sep=';')

    # Display first 5 rows
    print("-"*70)
    print("First 5 rows : ")
    print(df.head())

    # Dataset shape
    print("-"*70)
    print("Shape of dataset : ", df.shape)

    # Column names
    print("-"*70)
    print("Columns in dataset : ")
    print(df.columns)

    # Information about dataset
    print("-"*70)
    print("Dataset information : ")
    print(df.info())

    #################################################################
    # Handle unknown values in categorical columns
    #################################################################

    #  Replace 'unknown' with Nan
    df.replace("unknown",np.nan, inplace=True)

    # Fill categorical missing values with mode
    for col in df.select_dtypes(include=['object', 'string']).columns:
        df[col] = df[col].fillna(df[col].mode()[0])

    # Fill numerical missing values with median
    for col in df.select_dtypes(include=np.number).columns:
        df[col] = df[col].fillna(df[col].median())

    print("-"*70)
    print("Missing values after handling : ")
    print(df.isnull().sum())

    # Statistics using describe()
    print("-"*70)
    print("Statistical report of dataset : ")
    print(df.describe())

    # Visualize class distribution
    plt.figure(figsize=(6,4))
    sns.countplot(x="y", data=df)
    plt.title("Class Distribution")
    plt.show()

    #################################################################
    # Step 2 : Data Preprocessing
    #################################################################

    print(border)
    print("Step 2 : Data Preprocessing")
    print(border)

    #################################################################
    # Convert categorical vaiables
    #################################################################

    # Find categorical columns
    categorical_columns = df.select_dtypes(include=['object','string']).columns

    print("-"*70)
    print("Categorical columns : ")
    print(categorical_columns)

    # Apply Label Encoding
    label_encoder = LabelEncoder()

    for col in categorical_columns:
        df[col] = label_encoder.fit_transform(df[col])

    print("-"*70)
    print("Categorical columns get converted successfully")

    # Split features and target
    X = df.drop("y", axis=1)
    Y = df["y"]

    # Feature scaling
    scalar = StandardScaler()
    X_scaled = scalar.fit_transform(X)

    print("-"*70)
    print("Feature scaling completed successfully")

    #################################################################
    # Step 3 : Split the data
    #################################################################

    print(border)
    print("Step 3 : Split the data")
    print(border)

    X_train, X_test, Y_train, Y_test = train_test_split(X_scaled,Y,test_size=0.2,random_state=42)

    print("-"*70)
    print("Shape of X_train : ",X_train)
    print("Shape of X_test : ",X_test)
    print("Shape of Y_train : ",Y_train)
    print("Shape of Y_test : ",Y_test)

    #################################################################
    # Step 4 : Train Classification Model
    #################################################################

    print(border)
    print("Step 4 : Model Building")
    print(border)

    # Create base models
    model_lr = LogisticRegression(max_iter=10000)
    model_knn = KNeighborsClassifier(n_neighbors=5)
    model_rf = RandomForestClassifier(n_estimators=100,random_state=42)

    # Train base models
    model_lr.fit(X_train,Y_train)
    model_rf.fit(X_train,Y_train)
    model_knn.fit(X_train,Y_train)

    print("Models trained successfully")

    #################################################################
    # Step 5 : Evaluates the models
    #################################################################

    print(border)
    print("Step 5 : Evaluates the models")
    print(border)

    def evaluate_model(name, model,X_test,Y_test):

        print("-"*70)
        print("Model:", name)
        print("-"*70)

        Y_pred = model.predict(X_test)

        # Accuracy 
        accuracy = accuracy_score(Y_test,Y_pred)
        print("-"*70)
        print("Accuracy : ",accuracy)

        # Classification report
        print("-"*70)
        print("Classification report : \n",classification_report(Y_test,Y_pred))

        # Confusion matrix
        cm = confusion_matrix(Y_test,Y_pred)
        print("-"*70)
        print("Confusion matrix : \n",cm)

        # ROC-AUC Scores
        # Probability predictions
        Y_prob = model.predict_proba(X_test)[:,1]

        roc_score = roc_auc_score(Y_test,Y_prob)

        print("-"*70)
        print("ROC-AUC Score : ",roc_score)

    # Evaluate all models
    evaluate_model("Logistic Regression", model_lr, X_test, Y_test)
    evaluate_model("KNN Classifier", model_knn, X_test, Y_test)
    evaluate_model("Random Forest Classifier", model_rf, X_test, Y_test)

    #################################################################
    # Step 6 : Visualize Results
    #################################################################

    print(border)
    print("Step 6 : Visualize Results")
    print(border)

    def evaluate_model(name, model,X_test,Y_test):

        print("-"*70)
        print("Model:", name)
        print("-"*70)

        Y_pred = model.predict(X_test)


        # Confusion matrix
        cm = confusion_matrix(Y_test,Y_pred)

        # Visualization
        disp = ConfusionMatrixDisplay(confusion_matrix=cm)
        disp.plot()
        plt.title(f"Confusion Matrix - {name}")
        plt.show()

        # ROC Curve
        Y_prob = model.predict_proba(X_test)[:,1]
        fpr, tpr, thresholds = roc_curve(Y_test, Y_prob)
        roc_score = roc_auc_score(Y_test, Y_prob)

        plt.figure(figsize=(6,5))
        plt.plot(fpr, tpr, label=f"AUC = {roc_score:.2f}")
        plt.plot([0,1], [0,1], linestyle='--')
        plt.xlabel("False Positive Rate")
        plt.ylabel("True Positive Rate")
        plt.title(f"ROC Curve - {name}")
        plt.legend()
        plt.show()

    # Evaluate all models
    evaluate_model("Logistic Regression", model_lr, X_test, Y_test)
    evaluate_model("KNN Classifier", model_knn, X_test, Y_test)
    evaluate_model("Random Forest Classifier", model_rf, X_test, Y_test)

def main():
    DiabetesClassifier("bank-full.csv")

if __name__ == "__main__":
    main()