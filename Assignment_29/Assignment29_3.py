import os
import sys

def main():

    if(len(sys.argv) != 2):
        print("Usage : python program.py <ExistingFileName> ")
        return 
    
    Source = sys.argv[1]

    try:
        fobj = open(Source,"r")
        Data = fobj.read()
        fobj.close()

        cobj = open("Demo.txt","w")
        cobj.write(Data)
        cobj.close()

        print("The contents get copied successfully")

    except FileNotFoundError:
        print("Unable to open file as there is no such file")

    finally:
        print("End of application")

if __name__ == "__main__":
    main()