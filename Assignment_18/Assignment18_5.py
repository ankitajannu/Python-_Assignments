def CheckPrime(Arr):
    Sum = 0
    
    if(No <= 1):
        return False

    for i in range(2,len(Arr)):
        No = Arr[i]
        if(No % i == 0):
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

    Ret = CheckPrime(Data)
    print("Addition is : ",Ret)

if __name__ == "__main__":
    main()