Divisible = lambda No : No % 5 == 0

def main():
    Value = 0
    Ret = False

    print("Enter number : ")
    Value = int(input())

    Ret = Divisible(Value)
    
    print(Ret)

if __name__ == "__main__":
    main()