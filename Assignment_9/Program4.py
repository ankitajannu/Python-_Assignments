def Cube(No):
    for i in range(1,No+1):
        No = i**3

    return No

def main():
    Value = 0
    Ret = 0

    print("Enter number : ")
    Value = int(input())

    Ret = Cube(Value)
    print("Cube is : ",Ret)

if __name__ == "__main__":
    main()