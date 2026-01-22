def CheckPerfect(No):
    iTotal = 0

    if(No <= 0):
        return False
    
    for i in range(1,No):
        if(No % i == 0):
            iTotal = iTotal + i

    if(iTotal == No):
        return True
    else:
        return False            
        
def main():
    Value = 0
    Ret = True

    print("Enter number : ")
    Value = int(input())

    Ret = CheckPerfect(Value)

    if(Ret == True):
        print("The number is perfect")
    else:
        print("The number is not perfect")

if __name__ == "__main__":
    main()