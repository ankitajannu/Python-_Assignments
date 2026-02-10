import threading

def SumEven(Arr):
    Sum = 0
     
    for i in range(len(Arr)):
        if(Arr[i] % 2 == 0):
            Sum = Sum + Arr[i]

    print("Sum of even elements is : ",Sum)

def SumOdd(Arr):
    Sum = 0

    for i in range(len(Arr)):
        if(Arr[i] % 2 != 0):
            Sum = Sum + Arr[i]

    print("Sum of odd elemets is : ",Sum)

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

    EvenList = threading.Thread(target=SumEven, args=(Data,))
    OddList = threading.Thread(target=SumOdd, args=(Data,))

    EvenList.start()
    OddList.start()

    EvenList.join()
    OddList.join()

if __name__ == "__main__":
    main()