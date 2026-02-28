import os

def main():
    try:
        FileName = input("Enter the name of file : ")
        Ret = os.path.exists(FileName)

        if(Ret == True):
            fobj = open(FileName,"r")
            print("The file gets successfully opened")
        else:
            print("There's no such file")
            return

        Data = fobj.read()
        
        print(Data)

        fobj.close()

    except FileNotFoundError:
        print("Unable to open file as there is no such file")

    finally:
        print("End of application")

if __name__ == "__main__":
    main()