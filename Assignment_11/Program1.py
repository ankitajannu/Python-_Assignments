def CheckPrime(No):
    if(No <= 1):
        return False
    
    for i in range(2,No):
        if(No % i == 0):
            return False
    
    return True
        
def main():
    Value = 0
    Ret = True

    print("Enter number : ")
    Value = int(input())

    Ret = CheckPrime(Value)

    if(Ret == True):
        print("The number is prime")
    else:
        print("The number is not prime")

if __name__ == "__main__":
    main()