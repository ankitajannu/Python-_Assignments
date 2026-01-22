def SumDigits(No):
    iCount = 0
    iSum = 0

    if(No == 0):
        return 1
    
    while(No != 0):
        iCount = iCount + 1
        iSum = iSum + iCount
        No = No // 10

    return iSum
        
def main():
    Value = 0
    Ret = True

    print("Enter number : ")
    Value = int(input())

    Ret = SumDigits(Value)
    print("Sum of the digits are : ",Ret)

if __name__ == "__main__":
    main()