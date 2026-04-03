import sys
import os
import schedule

def DirectoryFileSearch(DirName, Extension):
    print("Searching .txt file from the directory : ",DirName)

    if os.path.exists(DirName) == False:
        print("directory does not exist")
        return
    
    for FolderName, SubFolderName, FileNames in os.walk(DirName):
        for File in FileNames:
            if File.endswith(Extension):
                print(os.path.join(FolderName,File))

def main():
    Border = "-"*50
    print(Border)
    print("----------Marvellous Data Shield System-----------")
    print(Border)

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This script is used to : ")
            print("1 : Takes auto backup at given time")
            print("2 : Backup only new and updated file")
            print("3 : Create an archive of the backup periodically")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as ")
            print("ScriptName.py TimeInterval SourceDirectory")
            print("TimeInterval : The time in minutes for periodic scheduling")
            print("SourceDirectory : Name of directory to backed up")

        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")

    # python Demo.py Demo .txt
    elif(len(sys.argv) == 3):
        print("Inside projects logic")
        DirName = sys.argv[1]
        Extension = sys.argv[2]

        print("Directory Name :",DirName)
        print("Extension : ",Extension)

        DirectoryFileSearch(DirName,Extension)
        
    else:
        print("Invalid number of command line argumaents")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more details")

    print(Border)
    print("---------Thank you for using our script-----------")
    print(Border)

if __name__ == "__main__":
    main()