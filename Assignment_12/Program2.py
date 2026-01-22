def Factors(No):
    for i in range(1, No+1):
        if(No % i == 0):
            print(i)
        
def main():
    Value = 0

    print("Enter number : ")
    Value = int(input())

    Factors(Value)

if __name__ == "__main__":
    main()