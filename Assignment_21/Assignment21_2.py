import threading

def Maximum(Arr):
    Max = Arr[0]
    for i in range(len(Arr)):
        if(Max > Arr[i]):
            Max = Arr[i]
    
    print("Maximum element from the list is : ",Max,end=" ")
    print()

def Minimum(Arr):
    Min = Arr[0]
    for i in range(len(Arr)):
            if(Min < Arr[i]):
                Min = Arr[i]
    
    print("Minimum element from the list is : ",Min,end=" ")
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

    Thread1 = threading.Thread(target=Maximum, args=(Data,))
    Thread2 = threading.Thread(target=Minimum, args=(Data,))

    Thread1.start()
    Thread2.start()

    Thread1.join()
    Thread2.join()

if __name__ == "__main__":
    main()