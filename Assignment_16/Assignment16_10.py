def CheckLength(ch):
    return(len(ch))

def main():
    print("Enter name : ")
    Name = input()

    Ret = CheckLength(Name)
    print("the length of the name is : ",Ret)

if __name__ == "__main__":
    main()