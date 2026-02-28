import os

def main():
    FileName = input("Enter the name of file : ")
    Ret = os.path.exists(FileName)

    if(Ret == True):
        fobj = open(FileName,"r")
        print("The file exists")
    else:
        print("There's no such file")

if __name__ == "__main__":
    main()