def SumFactors(No):
    Sum = 0

    for i in range(1,No):
        if(No % i == 0):
            Sum = Sum + i

    return Sum

def main():
    Value = 0
    Ret = 0

    print("Enter the number : ")
    Value = int(input())

    Ret = SumFactors(Value)
    print("Summation of the Factors is : ",Ret)

if __name__ == "__main__":
    main()