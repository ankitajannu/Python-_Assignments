Largest = lambda No1,No2,No3 : max(No1,No2,No3)

def main():
    Value1 = 0
    Value2 = 0
    Value3 = 0
    Ret = 0

    print("Enter first number : ")
    Value1 = int(input())

    print("Enter second number : ")
    Value2 = int(input())

    print("Enter third number : ")
    Value3 = int(input())

    Ret = Largest(Value1, Value2, Value3)

    print("Largest number is : ",Ret)

if __name__ == "__main__":
    main()