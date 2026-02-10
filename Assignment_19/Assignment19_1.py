PowerOfTwo = lambda No : No ** 2

def main():
    Value = 0
    Ret = 0

    print("Enter the number : ")
    Value = int(input())

    Ret = PowerOfTwo(Value)
    print("Power of two is : ",Ret)

if __name__ == "__main__":
    main()