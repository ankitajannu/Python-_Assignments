import sys
import os
import hashlib

def CalculateCheckSum(FileName):
    fobj = open(FileName,"rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def DirectoryDuplicate(DirName):
    Ret = False

    Ret = os.path.exists(DirName)
    if(Ret == False):
        print("There is no such directory")
        return
    
    Ret = os.path.isdir(DirName)
    if(Ret == False):
        print("It is not a directory")
        return
    
    Duplicate = {}
    
    for FolderName, SubFolderName, FileName in os.walk(DirName):
        for fname in FileName:
            fname = os.path.join(FolderName,fname)
            CheckSum = CalculateCheckSum(fname)

            if CheckSum in Duplicate:
                Duplicate[CheckSum].append(fname)
            else:
                Duplicate[CheckSum] = [fname]

    fobj = open("Log.txt","w")

    for value in Duplicate.values():
        if (len(value) > 1):
            fobj.write("Duplicate files : \n")
            for file in value:
                fobj.write(file + "\n")
            fobj.write("\n") 

    fobj.close()
    print("Log file gets created successfully")

    return Duplicate

def DirectoryDuplicateRemove(Path):
    MyDict = DirectoryDuplicate(Path)

    Result = list(filter(lambda x : (len(x)) > 1, MyDict.values()))

    Count = 0

    for value in Result:
        for file in value[1:]:
            print("Deleted files : ",file)
            os.remove(file)
            Count = Count + 1

    print("Total deleted files : ",Count)

def main():
    Border = "-"*50
    print(Border)
    print("----------Marvellous Data Shield System-----------")
    print(Border)

    if(len(sys.argv) == 2 and (sys.argv[1] == "--h" or sys.argv[1] == "--H")):
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

    # python Demo.py Demo 
    elif(len(sys.argv) == 2):
        print("Inside projects logic")
        DirName = sys.argv[1]

        print("Directory Name :",DirName)

        DirectoryDuplicateRemove(DirName)
        
    else:
        print("Invalid number of command line argumaents")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more details")

    print(Border)
    print("---------Thank you for using our script-----------")
    print(Border)

if __name__ == "__main__":
    main()