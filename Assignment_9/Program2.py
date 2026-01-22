def CheckGreater(No1,No2):
    iMax = 0

    if No1 > No2:
        iMax = No1
    else:
        iMax = No2

    return iMax

def main():
    Value1 = 0
    Value2 = 0
    Ret = 0

    print("Enter first number : ")
    Value1 = int(input())

    print("Enter second number : ")
    Value2 = int(input())

    Ret = CheckGreater(Value1,Value2)
    print("Greater number is : ",Ret)

if __name__ == "__main__":
    main()