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
        print("It is prime number")
    else:
        print("It is not a prime number")

if __name__ == "__main__":
    main()