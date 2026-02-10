from functools import reduce

CheckNumber = lambda No : No >= 70 and No <= 90
Increment = lambda No : No + 10
Product = lambda A,B : A*B 

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

    FData = list(filter(CheckNumber,Data))
    print("Multiplication is : ",FData)

    MData = list(map(Increment,FData))
    print("Incremented list is : ",MData)

    RData = reduce(Product,MData)
    print("Product is : ",RData)

if __name__ == "__main__":
    main()