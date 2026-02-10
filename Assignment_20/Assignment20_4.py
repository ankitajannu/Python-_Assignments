import threading

def CountSmall(Arr):
    Count = 0
     
    for i in range(len(Arr)):
        if(Arr[i] >= 'a' and Arr[i] <= 'z'):
            Count = Count + 1

    print("Count of small elements is : ",Count)

def CountCapital(Arr):
    Count = 0

    for i in range(len(Arr)):
        if(Arr[i] >= 'A' and Arr[i] <= 'Z'):
            Count = Count + 1

    print("Count of capital elemets is : ",Count)

def CountDigit(Arr):
    Count = 0

    for i in range(len(Arr)):
        if(Arr[i] >= '0' and Arr[i] <= '9'):
            Count = Count + 1

    print("Count of digit are : ",Count)

def main():
    print("Enter string : ")
    StringX = input()

    Small = threading.Thread(target=CountSmall, args=(StringX,))
    Capital = threading.Thread(target=CountCapital, args=(StringX,))
    Digit = threading.Thread(target=CountDigit, args=(StringX,))

    Small.start()
    Capital.start()
    Digit.start()

    Small.join()
    Capital.join()
    Digit.join()

if __name__ == "__main__":
    main()