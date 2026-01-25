Divisible = lambda No : No % 3 == 0 and No % 5 == 0

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

    FData = list(filter(Divisible, Data))
    print("Elements divisible by 3 and 5 : ",FData)

if __name__ == "__main__":
    main()