import sys
import os
import shutil

def DirectoryCopy(SourceDir,DestDir):
    print("Copying files from ",SourceDir," to ",DestDir)

    if os.path.exists(SourceDir) == False:
        print(" Source directory does not exist")
        return
    
    if os.path.exists(DestDir) == False:
        os.mkdir(DestDir)
        print("Directory gets successfully created")
    
    for FolderName, SubFolderName, FileNames in os.walk(SourceDir):
        for File in FileNames:
            SourceFile = os.path.join(FolderName,File)
            DestFile = os.path.join(DestDir,File)

            shutil.copy2(SourceFile,DestFile)
            print("Copied : ",SourceFile," to : ",DestFile)

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

    # python Demo.py Demo Temp
    elif(len(sys.argv) == 3):
        print("Usage : DirectoryCopy.py <SourceDir> <DestDir>")
        SourceDir = sys.argv[1]
        DestDir = sys.argv[2]

        DirectoryCopy(SourceDir,DestDir)

    else:
        print("Invalid number of command line argumaents")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more details")

    print(Border)
    print("---------Thank you for using our script-----------")
    print(Border)

if __name__ == "__main__":
    main()