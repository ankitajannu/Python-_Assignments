import pandas as pd

def MarvellousClassifier(DataPath):
    border = "-"*50

    ##################################################################
    # Step 1 : Load the Dataset
    ##################################################################

    print(border)
    print("Step 1 : Load the datasets")
    print(border)

    df = pd.read_csv(DataPath)

    ##################################################################
    # Step 2 : Display dataset deatils
    ##################################################################

    print(border)
    print("Step 2 : Display dataset deatils")
    print(border)

    print(df.head())
    print(df.tail()) 
    print("Total number of columns and rows : ",df.shape)
    print("Column names : ",list(df.columns))
    print("Dataypes of each columns : ",df.dtypes)

    ##################################################################
    # Step 3 : Analyse students results
    ##################################################################

    print(border)
    print("Step 3 : Analyse students results")
    print(border)

    print("total number of students in the dataset : ",df.shape[0])

    Passed = (df["FinalResult"] == 1).sum()
    print("Total number of students passed : ",Passed)

    Failed = (df["FinalResult"] == 0).sum()
    print("Total number of students failed : ",Failed)

    ##################################################################
    # Step 4 : Calculate statistical information
    ##################################################################

    print(border)
    print("Step 4 : Calculate statistical information")
    print(border)

    print("Average Study hours : ",df["StudyHours"].mean())

    print("Average Attendance : ",df["Attendance"].mean())

    print("Maximum Previous scores : ",df["PreviousScore"].max())

    print("Minimum Sleep hours : ",df["SleepHours"].min())

    ##################################################################
    # Step 5 : Analyse the final result distribution
    ##################################################################

    print(border)
    print("Step 5 : Analyse the final result distribution")
    print(border)

    result_count = df["FinalResult"].value_counts()

    print("Distribution of final result : ")
    print(result_count)

    pass_percentage = (result_count[1] / len(df)) * 100
    fail_percentage = (result_count[0] / len(df)) * 100

    print("Pass percentage : ",pass_percentage)
    print("Fail percentage : ",fail_percentage)

    if abs(pass_percentage - fail_percentage) <= 10:
        print("Justification : The percentage difference between pass and fail students is small, so the dataset is balanced")
    else:
        print("Justification : One class has significantly more students than the other, so the dataset is imbalanced")

def main():
    border = "-"*40

    print(border)
    print("Student Performance using DecisionTreeClassifier")
    print(border)

    MarvellousClassifier("student_performance_ml.csv")

if __name__ == "__main__":
    main()