import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from sklearn.preprocessing import LabelEncoder

def CheckAccuracy(df):
    border = "-"*50

    # Step 5  :Check Accuracy
    print(border)
    print("Step 5 : Check Accuracy") 
    print(border)

    X = df.drop(columns=[df.columns[-1]])
    Y = df[df.columns[-1]]

    X_train, X_test ,Y_train, Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

    for k in [1,3,5,7]:
        print(f"Cheacking for K = {k}")

        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train,Y_train)

        Y_pred = model.predict(X_test)

        accuracy = accuracy_score(Y_pred,Y_test)

        print(f"Accuracy for K = {k} : {accuracy * 100:.2f}%")
        print(border)

def MarvellousClassifier(DataPath):
    border = "-"*50

    # Step 1 : Load the dataset

    print(border)
    print("Step 1 : Load the dataset")
    print(border)

    df = pd.read_csv(DataPath)

    print(border)
    print("Some enteries from dataset : ")
    print(df.head())
    print(border)

    # Step 2 : Clean the dataset

    print(border)
    print("Step 2 : Clean the dataset")
    print(border)

    print("Shape of dataset before removal of the unnamed column: ",df.shape)

    if 'Unnamed: 0' in df.columns:
        df.drop(columns=['Unnamed: 0'], inplace=True)

    print("Shape of dataset after removal of the unnamed column: ",df.shape)
    
    le = LabelEncoder()

    for column in df.columns:
        df[column] = le.fit_transform(df[column])

    print("Dataset after LabelEncoding : ")
    print(df.head())
    print(border)

    # Step 3 : Train the dataset

    print(border)
    print("Step 3 : Train the model")
    print(border)

    X = df.drop(columns=[df.columns[-1]])
    Y = df[df.columns[-1]]

    model = KNeighborsClassifier(n_neighbors=3)

    model.fit(X,Y)

    print("model trained successfully")
    print(border)

    # step 4 : Test the data with user input

    print(border)
    print("Step 4 : Train the data with user input")
    print(border)

    input_data = []

    for column in X.columns:
        value = input(f"Enter value for (like 0,1,2) {column} : ")
        input_data.append(value)

    # Convert input to dataframe
    input_df = pd.DataFrame([input_data], columns=X.columns)

    # Applied LabelEncoding 

    encoder = {}

    for column in df.columns:
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])
        encoder[column] = le

    for column in input_df.columns:
        input_df[column] = encoder[column].transform(input_df[column])

    Result = model.predict(input_df)

    if(Result[0] == 1) : 
        print("Result = True")
    else:
        print("Result = False")

    CheckAccuracy(df)

def main():
    border = "-"*50
    print(border)
    print("Play Predictor using KNN")   
    print(border)

    MarvellousClassifier("PlayPredictor.csv")

if __name__ == "__main__":
    main() 