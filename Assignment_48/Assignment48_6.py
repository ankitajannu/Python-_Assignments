import numpy as np
from sklearn.metrics import classification_report

def DisplayClasificationReport():
    actual = [1,1,1,1,0,0,0,0]
    predicted = [1,1,0,1,0,1,0,0]

    Report = classification_report(actual,predicted)

    print("CLassifictaion report of the dataset : ")
    print(Report)

def main():
    DisplayClasificationReport()

if __name__ == "__main__":
    main()