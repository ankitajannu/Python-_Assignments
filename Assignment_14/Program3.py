Maximum = lambda No1,No2 : max(No1, No2)

def main():
    Value1 = 0
    Value2 = 0
    Ret = 0

    print("Enter first number : ")
    Value1 = int(input())

    print("Enter second number : ")
    Value2 = int(input())

    Ret = Maximum(Value1, Value2)

    print("Maximum is : ",Ret)

if __name__ == "__main__":
    main()