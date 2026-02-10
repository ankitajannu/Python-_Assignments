def CheckNum(No):
    if(No % 2 == 0):
        return True
    else:
        return False

def main():
    Value = 0
    Ret = 0

    print("Enter the number : ")
    Value = int(input())

    Ret = CheckNum(Value)

    if(Ret == True):
        print("Even number")
    else:
        print("Odd number")

if __name__ == "__main__":
    main()