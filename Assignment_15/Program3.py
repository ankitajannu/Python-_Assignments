Odd = lambda No : No % 2 != 0

def main():
    Size = 0
    Value = 0

    print("Enter the number of elements : ")
    Size = int(input())

    Data = list()

    print("Enter the elements")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    FData = list(filter(Odd, Data))
    print("Odd numbers from the list are : ",FData)

if __name__ == "__main__":
    main()