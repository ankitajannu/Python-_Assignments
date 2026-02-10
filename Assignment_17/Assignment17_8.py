def Display(No):
    for i in range(1,No+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()

def main():
    Value = 0

    print("Enter the number : ")
    Value = int(input())

    Display(Value)

if __name__ == "__main__":
    main()