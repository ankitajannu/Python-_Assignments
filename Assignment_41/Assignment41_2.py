import numpy as np
import math

def EucDistance(P1, P2):
    Ans = math.sqrt((P1['X'] - P2['X']) ** 2 + (P1['Y'] - P2['Y']) ** 2)
    return Ans

def MarvellousKNeighborsClassification():
    Border = "-"*50

    data = [
                {'Point' : 'A', 'X' : 1, 'Y' : 2, 'Label' : 'Red'},
                {'Point' : 'B', 'X' : 2, 'Y' : 3, 'Label' : 'Red'},
                {'Point' : 'C', 'X' : 3, 'Y' : 1, 'Label' : 'Blue'},
                {'Point' : 'D', 'X' : 6, 'Y' : 5, 'Label' : 'Blue'},
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

    print("Enter X coordinates: ")
    X = int(input())

    print("Enter Y coordinates: ")
    Y = int(input())

    new_point = {'X': X, 'Y': Y}

    print(new_point)

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

    K = 1
    nearest1 = sorted_data[:K]

    print(Border)
    print("Nearest 1 elements are : ")
    print(Border)

    for d in nearest1:
        print(d)

    K = 3
    nearest3 = sorted_data[:K]

    print(Border)
    print("Nearest 3 elements are : ")
    print(Border)

    for d in nearest3:
        print(d)

    K = 5
    nearest5 = sorted_data[:K]

    print(Border)
    print("Nearest 5 elements are : ")
    print(Border)

    for d in nearest5:
        print(d)

    votes1 = {}
    for neighbour in nearest1:
        label = neighbour['Label']
        votes1[label] = votes1.get(label,0) + 1

    votes2 = {}
    for neighbour in nearest3:
        label = neighbour['Label']
        votes2[label] = votes2.get(label,0) + 1

    votes3 = {}
    for neighbour in nearest5:
        label = neighbour['Label']
        votes3[label] = votes3.get(label,0) + 1

    print(Border)
    print("Voting result is : ")
    print(Border)

    for d in votes1:
        print("Names : ",d, "Number of votes : ",votes1[d])

    for d in votes2:
        print("Names : ",d, "Number of votes : ",votes2[d])

    for d in votes3:
        print("Names : ",d, "Number of votes : ",votes3[d])

    print(Border)

    predicted_class1 = max(votes1, key=votes1.get)
    print(f"Predicted class for K=1 is : {predicted_class1}")

    predicted_class3 = max(votes2, key=votes2.get)
    print(f"Predicted class for K=3 is : {predicted_class3}")

    predicted_class5 = max(votes3, key=votes3.get)
    print(f"Predicted class for K=5 is : {predicted_class5}")    

def main():
    MarvellousKNeighborsClassification()

if __name__ == "__main__":
    main()