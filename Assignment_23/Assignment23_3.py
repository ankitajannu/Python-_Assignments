class Numbers:
    def __init__(self,No):
        self.Value = No

    def CheckPrime(self):
        if(self.Value <= 1):
            return False
    
        for i in range(2,self.Value):
            if(self.Value % i == 0):
                return False
        
        return True

    def CheckPerfect(self):
        Sum = 0
        for i in range(1,self.Value):
            if(self.Value % i == 0):
                Sum = Sum + i

        if(Sum == self.Value):
            return True
        else:
            return False

    def Factors(self):
        print("Factors are : ",end=" ")
        for i in range(1,self.Value + 1):
            if(self.Value % i == 0):
                print(i,end=" ")

        print()

    def SumFactors(self):
        SumFact = 0
        for i in range(1,self.Value + 1):
            if(self.Value % i == 0):
                SumFact = SumFact + i

        return SumFact

def main():
    print("Enter first number : ")
    No1 = int(input())

    obj1 = Numbers(No1)

    Ret = obj1.CheckPrime
    if(Ret == True):
        print(No1," is prime number")
    else:
        print(No1," is not a prime number")

    Ret = obj1.CheckPerfect()
    if(Ret == True):
        print(No1," is perfect number")
    else:
        print(No1," is not a perfect number")

    obj1.Factors()
    print("Sum of factors are : ",obj1.SumFactors())

    print()

    print("Enter second number : ")
    No2 = int(input())

    obj2 = Numbers(No2)

    Ret = obj2.CheckPrime()
    if(Ret == True):
        print(No2," is prime number")
    else:
        print(No2," is not a prime number")

    Ret = obj2.CheckPerfect()
    if(Ret == True):
        print(No2," is perfect number")
    else:
        print(No2," is not a perfect number")

    obj2.Factors()

    print("Sum of factors are : ",obj2.SumFactors())

if __name__ == "__main__":
    main()