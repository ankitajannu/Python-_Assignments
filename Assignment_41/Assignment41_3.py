import numpy as np
import math

def EucDistance(P1, P2):
    Ans = math.sqrt((P1['Study Hours'] - P2['Study Hours']) ** 2 + (P1['Attendance'] - P2['Attendance']) ** 2)
    return Ans

def MarvellousKNeighborsClassification():
    Border = "-"*50

    data = [
                {'Study Hours' : 2,'Attendance' :60, 'Result' : "Fail"},
                {'Study Hours' : 5,'Attendance' :80, 'Result' : "Pass"},
                {'Study Hours' : 6,'Attendance' :85, 'Result' : "Pass"},
                {'Study Hours' : 1,'Attendance' :50, 'Result' : "Fail"}
    ]

    print(Border)
    print("User defined KNN")
    print(Border)

    print(Border)
    print("Training the data")
    print(Border)

    for i in data:
        print(i)

    print(Border)

    print("Enter Study hours : ")
    X = int(input())

    print("Enter Attendance percentage : ")
    Y = int(input())

    new_point = {'Study Hours': X, 'Attendance': Y}

    print("New point : ",new_point)

    for d in data:
        d['distance'] = EucDistance(d,new_point)

    print(Border)
    print("Calculated distance are : ")
    print(Border)

    for d in data:
        print(d)

    sorted_data = sorted(data, key = lambda item : item['distance'])

    print(Border)
    print("Sorted data is : ")
    print(Border)

    for d in sorted_data:
        print(d)

    K = 3
    nearest = sorted_data[:K]

    print(Border)
    print("Nearest meighbours : ")
    print(Border)

    for d in nearest:
        print(d)

    votes = {}
    for neighbour in nearest:
        label = neighbour['Result']
        votes[label] = votes.get(label,0) + 1

    print(Border)
    print("Voting result is : ")
    print(Border)

    for d in votes:
        print("Names : ",d, "Number of votes : ",votes[d])

    print(Border)

    predicted_class = max(votes, key=votes.get)

    print(f"Predicted Result : {predicted_class}")

def main():
    MarvellousKNeighborsClassification()

if __name__ == "__main__":
    main()