def ReverseNumber(No):
    iRev = 0
    iDigit = 0
    
    while(No != 0):
        iDigit = No % 10
        iRev = iRev * 10 + iDigit
        No = No // 10

    return iRev
        
def main():
    Value = 0
    Ret = True

    print("Enter number : ")
    Value = int(input())

    Ret = ReverseNumber(Value)
    print("Reverse number is : ",Ret)

if __name__ == "__main__":
    main()