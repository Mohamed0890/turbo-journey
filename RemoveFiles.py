import os
import shutil
import time

def main():
    dfileCount=0
    dFolderCount=0

    path="D:\86"

    days=30

    seconds=time.time()-(days*86400)
    if os.path.exists(path):
        for in rootFolder,folders,files in os.walk(path):
            if seconds>=get_file_or_folder_age(rootFolder):
                remove_folder(rootFolder)
                dFolderCount+=1
                break
            else:
                for folder in folders:
                    folder_path=os.path.join(rootFolder, folder)
                    if seconds>=get_file_or_folder_age(folder_path):
                        remove_folder(folder_path)
                        dFolderCount+=1
                for file in files:
                    files_path=os.path.join(rootFolder, file)
                    if seconds>=get_file_or_folder_age(files_path):
                        remove_file(files_path)
                        dFileCount+=1

    else:
        print("path not found")
    print("total folders deleted",dFolderCount)
    print("total files deleted", dfileCount)

def remove_folder(path):
 
    # removing the folder
    if not shutil.rmtree(path):
 
        # success message
        print(f"{path} is removed successfully")
 
    else:
 
        # failure message
        print(f"Unable to delete the "+path)
 
 
 
def remove_file(path):
 
    # removing the file
    if not os.remove(path):
 
        # success message
        print(f"{path} is removed successfully")
 
    else:
 
        # failure message
        print("Unable to delete the "+path)
 
 
def get_file_or_folder_age(path):
 
    # getting ctime of the file/folder
    # time will be in seconds
    ctime = os.stat(path).st_ctime
 
    # returning the time
    return ctime
