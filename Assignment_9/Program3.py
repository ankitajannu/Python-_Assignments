def Square(No):
    for i in range(1,No+1):
        No = i*i

    return No

def main():
    Value = 0
    Ret = 0

    print("Enter number : ")
    Value = int(input())

    Ret = Square(Value)
    print("Square is : ",Ret)

if __name__ == "__main__":
    main()