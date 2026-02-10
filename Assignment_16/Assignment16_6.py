def CheckNum(No):
    if(No > 0):
        return "Positive"
    elif(No < 0):
        return "Negative"
    else:
        return "Zero"

def main():
    Value = 0
    Ret = 0

    print("Enter the number : ")
    Value = int(input())

    Ret = CheckNum(Value)

    print("The number is : ",Ret)

if __name__ == "__main__":
    main()