def Min(Arr):
    Min = Arr[0]

    for i in range(len(Arr)):
        if(Arr[i] < Min):
            Min = Arr[i]

    return Min

def main():
    Value = 0
    Size = 0
    Ret = 0

    print("Enter the number of elements : ")
    Size = int(input())

    Data = list()

    print("Enter the elements : ")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    Ret = Min(Data)
    print("Minimum is : ",Ret)

if __name__ == "__main__":
    main()