Cube = lambda No : No ** 3

def main():
    Value = 0
    Ret = 0

    print("Enter number : ")
    Value = int(input())

    Ret = Cube(Value)
    print("Cube of the given number is : ",Ret)

if __name__ == "__main__":
    main()