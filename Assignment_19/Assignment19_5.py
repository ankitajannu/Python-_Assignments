from functools import reduce

def Prime(No):
    if(No <= 1):
        return False
    
    for i in range(2,No):
        if(No % i == 0):
            return False
    
    return True

def Multiplication(No):
    Ans = 0
    Ans = No * 2
    return Ans

def Maximum(No1, No2):
    if(No1 > No2):
        return No1
    else:
        return No2
        
def main():
    Size = 0
    Value = 0
    Ret = 0

    print("Enter the number of elements : ")
    Size = int(input())

    Data = list()

    print("Enter the elements : ")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    FData = list(filter(Prime,Data))
    print("Prime elements from the list are : ",FData)

    MData = list(map(Multiplication,FData))
    print("Multiplication is : ",MData)

    RData = reduce(Maximum,MData)
    print("Maximum is : ",RData)

if __name__ == "__main__":
    main()