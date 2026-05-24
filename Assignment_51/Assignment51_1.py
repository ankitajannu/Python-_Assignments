import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix,ConfusionMatrixDisplay

def FakeNewsDetection():
    border = "="*70

    #################################################################
    # Step 1 : Data Preprocessing
    #################################################################

    print(border)
    print("Step 1 : Data Preprocessing")
    print(border)

    # Load the dataset
    fake_df = pd.read_csv("Fake.csv")
    true_df = pd.read_csv("True.csv")

    print("Fake Dataset shape : ",fake_df.shape)
    print("True Dataset shape : ",true_df.shape)

    # Add label column
    
    # Fake news = 0
    fake_df["label"] = 0

    # Real news = 1
    true_df["label"] = 1

    # Combine both datasets
    df = pd.concat([fake_df,true_df], ignore_index=True)

    print("-"*70)
    print("Combined Dataset shaped : ",df.shape)

    # Use relevant columns
    # combine title and text columns
    df["content"] = df["title"] + " " + df["text"]

    # Drop null values
    df = df.dropna()

    print("-"*70)
    print("Null values : ")
    print(df.isnull().sum())

    # Input and Output features
    X = df["content"]
    Y = df["label"]

    print("-"*70)
    print("Total input samples : ", X.shape)
    print("Total Output samples : ",Y.shape)

    #################################################################
    # Step 2 : Feature Extraction
    #################################################################

    print(border)
    print("Step 2 : Feature Extraction using TF-IDF")
    print(border)

    tfidf = TfidfVectorizer(stop_words='english', max_df=0.7)

    X_features = tfidf.fit_transform(X)

    print("-"*70)
    print("Shape after TF-IDF Vectorzation : ",X_features.shape)

    # Train test split
    X_train, X_test, Y_train, Y_test = train_test_split(X_features,Y,test_size=0.2,random_state=42)

    print("-"*70)
    print("Shape of X_train : ",X_train)
    print("Shape of X_test : ",X_test)
    print("Shape of Y_train : ",Y_train)
    print("Shape of Y_test : ",Y_test)

    #################################################################
    # Step 3 : Model Training
    #################################################################

    print(border)
    print("Step 3 : Model Training")
    print(border)

    #################################################################
    # Logistic Regression
    #################################################################

    model_lr = LogisticRegression(max_iter=5000)

    model_lr.fit(X_train,Y_train)

    Y_pred_lr = model_lr.predict(X_test)

    accuracy_lr = accuracy_score(Y_test, Y_pred_lr)

    print("-"*70)
    print("Logistic Regression accuracy : ",accuracy_lr)

    #################################################################
    # Decision Tree Classifier
    #################################################################

    model_dt = DecisionTreeClassifier(random_state=42)

    model_dt.fit(X_train,Y_train)

    Y_pred_dt = model_dt.predict(X_test)

    accuracy_dt = accuracy_score(Y_test, Y_pred_dt)

    print("-"*70)
    print("Decision Tree Classifier accuracy : ",accuracy_dt)

    #################################################################
    # Hard Voting Classifier
    #################################################################

    hard_voting = VotingClassifier(
        estimators=[
            ('lr', model_lr),
            ('dt', model_dt)
        ],
        voting='hard'
    )

    hard_voting.fit(X_train,Y_train)

    Y_pred_hard = hard_voting.predict(X_test)

    accuracy_hard = accuracy_score(Y_test, Y_pred_hard)

    print("-"*70)
    print("Hard Voting accuracy : ",accuracy_hard)

    #################################################################
    # Soft Voting Classifier
    #################################################################

    soft_voting = VotingClassifier(
        estimators=[
            ('lr', model_lr),
            ('dt', model_dt)
        ],
        voting='soft'
    )

    soft_voting.fit(X_train,Y_train)

    Y_pred_soft = soft_voting.predict(X_test)

    accuracy_soft = accuracy_score(Y_test, Y_pred_soft)

    print("-"*70)
    print("Soft Voting accuracy : ",accuracy_soft)

    #################################################################
    # Step 5 : Evaluation
    #################################################################

    print(border)
    print("Step 4 : Evaluation")
    print(border)

    print("Accuracy Comaprison : ")
    print("-"*70)

    print("Logistic Regression : ",accuracy_lr)
    print("Decision Tree Classifier : ",accuracy_dt)
    print("Hard Voting : ",accuracy_hard)
    print("Soft Voting : ",accuracy_soft)

    #################################################################
    # Confusion Matirx : Logistics Regression
    #################################################################

    cm_lr = confusion_matrix(Y_test,Y_pred_lr)
    
    print("-"*70)
    print("Confusion Matrix : Logistic Regression")
    print(cm_lr)

    display = ConfusionMatrixDisplay(
        confusion_matrix=cm_lr,
        display_labels=["Fake","Real"]
    )

    display.plot()
    plt.title("Logistic Regression Confusion Matrix")
    plt.show() 

    #################################################################
    # Confusion Matirx : Decision Tree Classifier
    #################################################################

    cm_dt = confusion_matrix(Y_test,Y_pred_dt)
    
    print("-"*70)
    print("Confusion Matrix : Decision Tree Classifier")
    print(cm_dt)

    display = ConfusionMatrixDisplay(
        confusion_matrix=cm_dt,
        display_labels=["Fake","Real"]
    )

    display.plot()
    plt.title("Decision Tree Classifier Confusion Matrix")
    plt.show() 

    #################################################################
    # Confusion Matirx : Hard Voting
    #################################################################

    cm_hard = confusion_matrix(Y_test,Y_pred_hard)
    
    print("-"*70)
    print("Confusion Matrix : Hard Voting")
    print(cm_hard)

    display = ConfusionMatrixDisplay(
        confusion_matrix=cm_hard,
        display_labels=["Fake","Real"]
    )

    display.plot()
    plt.title("Hard Voting Confusion Matrix")
    plt.show() 

    #################################################################
    # Confusion Matirx : Soft Voting
    #################################################################

    cm_soft = confusion_matrix(Y_test,Y_pred_soft)
    
    print("-"*70)
    print("Confusion Matrix : Soft Voting")
    print(cm_soft)

    display = ConfusionMatrixDisplay(
        confusion_matrix=cm_soft,
        display_labels=["Fake","Real"]
    )

    display.plot()
    plt.title("Soft Voting Confusion Matrix")
    plt.show() 

    #################################################################
    # Soft Voting  vs Hard Voting
    #################################################################

    print(border)
    print("Soft Voting vs Hard Voting")
    print(border)

    if accuracy_soft > accuracy_hard:
        print("Soft voting performed better")
    elif accuracy_hard > accuracy_soft:
        print("Hard voting performed better")
    else:
        print("Both voting techniques performed equally")

    #################################################################
    # Final Conclusion
    #################################################################

    print(border)
    print("Fianl Conclusion")
    print(border)

    best_accuracy = max(
        accuracy_lr,
        accuracy_dt,
        accuracy_hard,
        accuracy_soft
    )

    if best_accuracy == accuracy_lr:
        print("Logistic Regression is the best performing model")
    elif best_accuracy == accuracy_dt:
        print("Decision Tree Calssifier is the best performing model")
    elif best_accuracy == accuracy_hard:
        print("Hard Voting Calssifier is the best performing model")
    else:
        print("Soft Voting Calssifier is the best performing model")

def main():
    FakeNewsDetection()

if __name__ == "__main__":
    main()