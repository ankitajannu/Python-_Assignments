def Factorial(No):
    for i in range(1, No):
        No = No * i

    return No
        
def main():
    Value = 0
    Ret = 0

    print("Enter number : ")
    Value = int(input())

    Ret = Factorial(Value)
    print("Factorial is  : ",Ret)

if __name__ == "__main__":
    main()