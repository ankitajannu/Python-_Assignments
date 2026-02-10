def Divisible(No):
    if(No % 5 == 0):
        return True
    else:
        return False

def main():
    Value = 0
    Ret = 0

    print("Enter the number : ")
    Value = int(input())

    Ret = Divisible(Value)

    print(Ret)

if __name__ == "__main__":
    main()