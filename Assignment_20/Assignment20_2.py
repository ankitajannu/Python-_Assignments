import threading

def SumEvenFactors(No):
    Sum = 0
     
    for i in range(2,No+1,2):
        if(No % i == 0):
            Sum = Sum + i

    print("Sum of even factors is : ",Sum)

def SumOddFactors(No):
    Sum = 0

    for i in range(1,No+1,2):
        if(No % i == 0):
            Sum = Sum + i

    print("Sum of odd factors is : ",Sum)

def main():
    Value = 0

    print("Enter the number : ")
    Value = int(input())

    EvenFactor = threading.Thread(target=SumEvenFactors, args=(Value,))
    OddFactor = threading.Thread(target=SumOddFactors, args=(Value,))

    EvenFactor.start()
    OddFactor.start()

    EvenFactor.join()
    OddFactor.join()

    print("Exit from main")

if __name__ == "__main__":
    main()