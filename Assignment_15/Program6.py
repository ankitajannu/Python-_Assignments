from functools import reduce

Minimum = lambda No1, No2 : min(No1,No2)

def main():
    Size = 0
    Value = 0

    print("Enter the number of elements : ")
    Size = int(input())

    Data = list()

    print("Enter the elements")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    RData = reduce(Minimum, Data)
    print("Minimum element is : ",RData)

if __name__ == "__main__":
    main()