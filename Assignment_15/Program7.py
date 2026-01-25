GreaterString = lambda string : len(string) > 5

def main():
    Size = 0
    Value = 0

    print("Enter the number of string  : ")
    Size = int(input())

    Data = list()

    print("Enter the string")

    for i in range(Size):
        Value = input()
        Data.append(Value)

    FData = list(filter(GreaterString, Data))
    print("String having length greater than 5 : ",FData)

if __name__ == "__main__":
    main()