import threading

def Prime(Arr):
    print("Prime numbers from the list are : ",end=" ")

    for i in range(len(Arr)):
        No = Arr[i]

        if(No > 1):
            Count = 0
        
            for i in range(2,No):
                if(No % i == 0):
                    Count =Count + 1
        
            if(Count == 0):
                print(No,end=" ")

    print()

def NonPrime(Arr):
    print("Prime numbers from the list are : ",end=" ")

    for i in range(len(Arr)):
        No = Arr[i]

        if(No > 1):
            Count = 0
        
            for i in range(2,No):
                if(No % i == 0):
                    Count = Count + 1
        
            if(Count != 0):
                print(No,end=" ")

    print()

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

    Thread1 = threading.Thread(target=Prime, args=(Data,))
    Thread2 = threading.Thread(target=NonPrime, args=(Data,))

    Thread1.start()
    Thread2.start()

    Thread1.join()
    Thread2.join()

if __name__ == "__main__":
    main()