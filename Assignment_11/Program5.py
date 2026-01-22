def CheckPallindrome(No):
    Original = No
    iRev = 0
    iDigit = 0
    
    while(No != 0):
        iDigit = No % 10
        iRev = iRev * 10 + iDigit
        No = No // 10

    if(iRev == Original):
        return True
    else:
        return False
        
def main():
    Value = 0
    Ret = True

    print("Enter number : ")
    Value = int(input())

    Ret = CheckPallindrome(Value)

    if(Ret == True):
        print("It is Pallindrome")
    else:
        print("It is not Pallindrome")

if __name__ == "__main__":
    main()