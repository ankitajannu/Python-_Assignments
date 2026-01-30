def Display(No):
    for i in range(1, No+1):
        print(i)
        
def main():
    Value = 0

    print("Enter number : ")
    Value = int(input())

    Display(Value)

if __name__ == "__main__":

    main()
