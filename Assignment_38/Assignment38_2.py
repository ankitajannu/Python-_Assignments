import pandas as pd

def MarvellousClassifier(DataPath):
    border = "-"*50

    ##################################################################
    # Step 1 : Load the Dataset
    ##################################################################

    print(border)
    print("Step 1 : Load the dataset")
    print(border)

    df = pd.read_csv(DataPath)

    ##################################################################
    # Step 1 : Load the details
    ##################################################################

    print(border)
    print("Step 2 : Display dataset details")
    print(border)

    print(df.head())
    print(df.tail()) 
    print("Total number of columns and rows : ",df.shape)
    print("Column names : ",list(df.columns))
    print("Dataypes of each columns : ",df.dtypes)

    ##################################################################
    # Step 3 : Analyze students results
    ##################################################################

    print(border)
    print("Step 3 : Analyse students results")
    print(border)

    print("total number of students in the dataset : ",df.shape[0])

    Passed = (df["FinalResult"] == 1).sum()
    print("Total number of students passed : ",Passed)

    Failed = (df["FinalResult"] == 0).sum()
    print("Total number of students failed : ",Failed)

def main():
    border = "-"*40

    print(border)
    print("Student Performance using DecisionTreeClassifier")
    print(border)

    MarvellousClassifier("student_performance_ml.csv")

if __name__ == "__main__":
    main()