
CountEven = lambda No : No % 2 == 0 

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

    FData = list(filter(CountEven, Data))
    print("Count of Even elements from the list are : ",len(FData))

if __name__ == "__main__":
    main()