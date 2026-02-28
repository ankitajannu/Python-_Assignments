import os
import sys

def main():
    try:
        File1 = input("Enter the name of an existing file : ")
        fobj = open(File1,"r")

        File2 = input("Enter the name of new file : ")
        cobj = open(File2,"w")

        Data = fobj.read()
        fobj.close()

        cobj = open(File2,"w")
        cobj.write(Data)
        cobj.close()

        print("The contents get copied successfully")

    except FileNotFoundError:
        print("Unable to open file as there is no such file")

    finally:
        print("End of application")

if __name__ == "__main__":
    main()