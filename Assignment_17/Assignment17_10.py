def SumDigit(No):
    Sum = 0
    Count = 0

    if(No == 0):
        return 1
    
    while(No != 0):
        Count = Count + 1
        Sum = Sum + Count
        No = No // 10

    return Sum
        
def main():
    Value = 0
    Ret = True

    print("Enter number : ")
    Value = int(input())

    Ret = SumDigit(Value)
    print("Sum of number of digits are : ",Ret)

if __name__ == "__main__":
    main()