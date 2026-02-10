import threading

def Summation(Arr,Result):
    Sum = 0
    for i in range(len(Arr)):
        Sum = Sum + Arr[i]

    Result.append(Sum)

def Product(Arr,Result):
    Prod = 1

    for i in range(len(Arr)):
        Prod = Prod * Arr[i]
    
    Result.append(Prod)

def main():
    Size = 0
    Value = 0
    
    print("Enter the number of elements : ")
    Size = int(input())

    Data = list()

    print("Enter the elements : ")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    RetSum = list()
    RetProduct = list()


    Thread1 = threading.Thread(target=Summation, args=(Data,RetSum))
    Thread2 = threading.Thread(target=Product, args=(Data,RetProduct))

    Thread1.start()
    Thread2.start()

    Thread1.join()
    Thread2.join()

    print("Sum of elements are : ",RetSum[0])
    print("Product of elements are : ",RetProduct[0])

if __name__ == "__main__":
    main()