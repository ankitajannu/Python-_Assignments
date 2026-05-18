import pandas as pd
import matplotlib.pyplot as plt

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

    ##################################################################
    # Step 6 : Analyse StudyHours and Attendance
    ##################################################################

    print(border)
    print("Step 6 : Analyse StudyHours and Attendance")
    print(border)

    print(df.groupby("FinalResult")[["StudyHours","Attendance"]].mean())

    print("Observation : ")
    print("1.Students with higher study hours generally have better chances of passing.")
    print("2.Students with higher attendance also show improved final results.")
    print("3.The average StudyHours and Attendance of passed students are higher than the failed students.")
    print("4.This indicates that regular study and attendance positively affect student performance.")
    print("5.Therefore, StudyHours nad Attendance are important factors in predicting FinalResults")

    ##################################################################
    # Step 7 : Plot Histogram of StudyHours
    ##################################################################

    print(border)
    print("Step 7 : Plot Histogram of StudyHours")
    print(border)

    plt.hist(df["StudyHours"], bins=10)
    plt.title("Histogram of StudyHours")
    plt.xlabel("Study Hours")
    plt.ylabel("Number of students")
    plt.grid(True)
    plt.show()

    print("Observation : ")
    print("1.The histogram shows distribution of study hours among students.")
    print("2.Most students are concentrated around the middle range of study hours.")
    print("3.Very few students study extremely low or extremely high hours.")
    print("4.This indicates that the majority of students follow a moderate study pattern.")
    print("5.StudyHours are not uniformly distributed across all students.")


def main():
    border = "-"*40

    print(border)
    print("Student Performance using DecisionTreeClassifier")
    print(border)

    MarvellousClassifier("student_performance_ml.csv")

if __name__ == "__main__":
    main()