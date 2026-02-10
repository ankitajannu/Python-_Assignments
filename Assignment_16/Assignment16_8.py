def Display(No):
    for i in range(No):
        print("*",end=" ")

def main():
    Value = 0

    print("Enter the number : ")
    Value = int(input())

    Display(Value)

if __name__ == "__main__":
    main()