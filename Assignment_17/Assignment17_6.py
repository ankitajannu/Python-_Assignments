def Display(No):
    for i in range(No,0,-1):
        print("*\t"*i)

def main():
    Value = 0

    print("Enter the number : ")
    Value = int(input())

    Display(Value)

if __name__ == "__main__":
    main()