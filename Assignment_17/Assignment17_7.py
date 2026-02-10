def Display(No):
    for i in range(No):
        for j in range(1,No+1):
            print(j,end=" ")
        print()

def main():
    Value = 0

    print("Enter the number : ")
    Value = int(input())

    Display(Value)

if __name__ == "__main__":
    main()