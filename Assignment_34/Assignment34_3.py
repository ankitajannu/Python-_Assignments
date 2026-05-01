import sys
import os
import time
import schedule
import shutil
import hashlib
import zipfile
import smtplib
from email.message import EmailMessage

def RestoreBackup(zip_file, destination):
    Border = "-"*50

    print(Border)
    print("Restore process started at : ",time.ctime())
    print(Border)

    if not os.path.exists(zip_file):
        print("Error : zip file not found")
        return
    
    os.makedirs(destination,exist_ok=True)

    try:
        with zipfile.ZipFile(zip_file, 'r') as zobj:
            zobj.extractall(destination)

        print(Border)
        print("Restore completed successfully")
        print("Files restored to : ",destination)
        print(Border)

    except Exception as e:
        print("Restore failed : ",e)

def SendMail(log_file, zip_file):
    Sender_mail = "marvellouspython20@gmail.com"
    App_password = "wanm kyul nyfh grac"
    Receiver_mail = "jannutriveni608@gmail.com"

    message = EmailMessage()
    message["Subject"] = "Backup completed successfully"
    message["From"] = Sender_mail
    message["To"] = Receiver_mail

    message.set_content(f"""
Backup Process completed successfully 

Zip file created : {zip_file}
Log file Attached 

Time : {time.ctime()}
""")
    
    with open(log_file, "rb") as f:
        message.add_attachment(f.read(), maintype="application", subtype="octet-stream", filename = os.path.basename(log_file))

    with open(zip_file, "rb") as f:
        message.add_attachment(f.read(), maintype="application", subtype="zip", filename = os.path.basename(zip_file))

    try:
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(Sender_mail,App_password)
        server.send_message(message)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print("Unable to send email : ",e)

def make_zip(folder):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    zip_name = folder + "_" + timestamp + ".zip"

    # Open the zip file
    zobj = zipfile.ZipFile(zip_name,"w", zipfile.ZIP_DEFLATED)

    for root, dirs, files in os.walk(folder):
        for file in files:
            full_path = os.path.join(root,file)
            relative = os.path.relpath(full_path,folder)

            zobj.write(full_path,relative)

    zobj.close()

    return zip_name

def calculate_hash(path):
    hobj = hashlib.md5()

    fobj = open(path, "rb")

    while True:
        data = fobj.read(1024)
        if not data:
            break
        else:
            hobj.update(data)

    fobj.close()

    return hobj.hexdigest()

def BackupFiles(Source, Destination):
    copied_file = []

    print("Creating the Backup folder for backup process")

    os.makedirs(Destination, exist_ok=True)

    for root, dirs, files in os.walk(Source):
        for file in files:
            src_path = os.path.join(root, file)

            relative = os.path.relpath(src_path, Source)
            dest_path = os.path.join(Destination, relative)

            os.makedirs(os.path.dirname(dest_path), exist_ok=True)

            # Copy the files if its new 
            if((not os.path.exists(dest_path)) or (calculate_hash(src_path) != calculate_hash(dest_path))):
                shutil.copy2(src_path, dest_path)
                copied_file.append(relative)

    return copied_file

def CreateLog():
    dir = "Logs"

    os.makedirs(dir, exist_ok=True)

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S") 
    file = os.path.join(dir, f"log_{timestamp}.txt")

    return file

def MarvellousDataShieldStart(Source = "Data"):
    Border = "-"*50

    BackupName = "MarvellousBackup"

    file = CreateLog()

    try:
        start_time = time.ctime()

        print(Border)
        print("Backup process started successfully at : ",time.ctime())
        print(Border)

        files = BackupFiles(Source, BackupName)

        zip_file = make_zip(BackupName)

        print(Border)
        print("Backup completed successfully")
        print("Files copied : ",len(files))
        print("Zip file gets created : ",zip_file)
        print(Border)

        with open(file, 'w')as fobj:
            fobj.write(f"{Border}\n")
            fobj.write("--------------------Backup Log--------------------\n")
            fobj.write(f"Start time : {start_time}\n")
            fobj.write(f"End time : {time.ctime()}\n")
            fobj.write(f"Source : {Source}\n")
            fobj.write(f"Files copied : {len(files)}\n")
            fobj.write(f"Zip file : {zip_file}\n")

            fobj.write("Copied files List : \n")
            for f in files:
                fobj.write(f"{f}\n")
            fobj.write(f"{Border}\n")

        SendMail(file, zip_file)

    except Exception as e:
        os.makedirs("Logs", exist_ok=True)
        with open(file,"w") as fobj:
            fobj.write("\nERROR LOG\n")
            fobj.write(f"{time.ctime()}\n")
            fobj.write(f"Error : {str(e)}\n")

        print("Error occured. Check log file.")

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
            print("4 : Restore backup from zip file")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as ")
            print("ScriptName.py TimeInterval SourceDirectory")
            print("TimeInterval : The time in minutes for periodic scheduling")
            print("SourceDirectory : Name of directory to backed up")

        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")
            print("Restore usage : ")
            print("ScriptName.py --restore ZipFileName DestinationFolder")

    # python Demo.py 5 Data
    elif(len(sys.argv) == 3):
        print("Inside projects logic")
        print("Time interval : ",sys.argv[1])
        print("Directory name : ",sys.argv[2])

        # Apply the scheduler
        schedule.every(int(sys.argv[1])).minutes.do(MarvellousDataShieldStart, sys.argv[2])

        print(Border)
        print("Data Shield System started successfully")
        print("Time interval in minutes : ",sys.argv[1])
        print("Press Ctrl + C to stop the execution")
        print(Border)

        # Wait till abort
        while True:
            schedule.run_pending()
            time.sleep(1)

    elif(len(sys.argv) == 4 and sys.argv[1] == "--restore"):
        zip_file = sys.argv[2]
        destination = sys.argv[3]

        RestoreBackup(zip_file,destination)

    else:
        print("Invalid number of command line argumaents")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more details")

    print(Border)
    print("---------Thank you for using our script-----------")
    print(Border)

if __name__ == "__main__":
    main()