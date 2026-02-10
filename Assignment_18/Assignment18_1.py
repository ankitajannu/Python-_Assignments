def Add(Arr):
    Sum = 0
    for i in range(len(Arr)):
        Sum = Sum + Arr[i]

    return Sum

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

    Ret = Add(Data)
    print("Addition is : ",Ret)

if __name__ == "__main__":
    main()