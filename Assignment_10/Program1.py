def MultiplicationTable(No):
    for i in range(1,11):
        print(No * i)
        
def main():
    Value = 0
    
    print("Enter number : ")
    Value = int(input())

    MultiplicationTable(Value)

if __name__ == "__main__":
    main()