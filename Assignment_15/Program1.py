Square = lambda Data : Data ** 2

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

    MData = list(map(Square, Data))
    print("Square is : ",MData)

if __name__ == "__main__":
    main()