def Display(No):
    for i in range(1,No+1,1):
        print("*\t"*No)

def main():
    Value = 0

    print("Enter the number : ")
    Value = int(input())

    Display(Value)

if __name__ == "__main__":
    main()