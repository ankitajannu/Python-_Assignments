from functools import reduce

Even = lambda No : No % 2 == 0
CalculateSquare = lambda No : No ** 2
Addition = lambda A,B : A+B 

def main():
    Size = 0
    Value = 0
    Ret = 0

    print("Enter the number of elements : ")
    Size = int(input())

    Data = list()

    print("Enter the elements : ")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    FData = list(filter(Even,Data))
    print("Even elements from the list are : ",FData)

    MData = list(map(CalculateSquare,FData))
    print("Calculated square are : ",MData)

    RData = reduce(Addition,MData)
    print("Addition is : ",RData)

if __name__ == "__main__":
    main()