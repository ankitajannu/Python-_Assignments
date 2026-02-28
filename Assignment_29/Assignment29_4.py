import os
import sys

def main():

    if(len(sys.argv) != 3):
        print("Usage : python program.py <ExistingFileName> ")
        return 
    
    File1 = sys.argv[1]
    File2 = sys.argv[2]

    try:
        fobj1 = open(File1,"r")
        Data1 = fobj1.read()
        fobj1.close()

        fobj2 = open(File2,"r")
        Data2 = fobj2.read()
        fobj2.close()

        if(Data1 == Data2):
            print("Success")
            print("Both file contains the same context")
        else:
            print("Failure")
            print("Both file does not contains the same context")


    except FileNotFoundError:
        print("Unable to open file as there is no such file")

    finally:
        print("End of application")

if __name__ == "__main__":
    main()