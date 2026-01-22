def CheckDivisible(No):
    if ((No % 3 == 0) and (No % 5 == 0)):
        return True
    else:
        return False

def main():
    Value = 0
    Ret = True

    print("Enter number : ")
    Value = int(input())

    Ret = CheckDivisible(Value)

    if(Ret == True):
        print("The number is divisible by 3 and 5")
    else:
        print("The number is not divisible by 3 and 5")

if __name__ == "__main__":
    main()