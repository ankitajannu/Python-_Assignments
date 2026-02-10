def Frequency(Arr,No):
    Count = 0

    for i in range(len(Arr)):
        if(Arr[i] == No):
            Count = Count + 1

    return Count

def main():
    Value = 0
    Search = 0
    Size = 0
    Ret = 0

    print("Enter the number of elements : ")
    Size = int(input())

    Data = list()

    print("Enter the elements : ")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    print("Element to search : ")
    Search = int(input())

    Ret = Frequency(Data,Search)
    print("Frequency of the given number is : ",Ret)

if __name__ == "__main__":
    main()