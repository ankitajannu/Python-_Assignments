def CountDigit(No):
    iCount = 0

    if(No == 0):
        return 1
    
    while(No != 0):
        iCount = iCount + 1
        No = No // 10

    return iCount
        
def main():
    Value = 0
    Ret = True

    print("Enter number : ")
    Value = int(input())

    Ret = CountDigit(Value)
    print("Total number of digits are : ",Ret)

if __name__ == "__main__":
    main()