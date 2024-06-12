import sys
import os
import shutil
import datetime

if len(sys.argv) < 2:
     print("ERROR: You must specify the full system path to the folder as a command line argument.\nPlease try running again with the following format: 'python organize_by_date.py FOLDER_TO_ORGANIZE")
     exit()

directory = str(sys.argv[1])

while(os.path.exists(directory) == False):
        directory = input("Invalid directory path. Please enter the full system path to the directory: ")

if os.path.exists(directory):
    os.chdir(directory)

    files = os.listdir()
    cur_d = os.getcwd()

    for file in files:
        try:
            path = os.path.join(cur_d, file)

            # if it's a folder, move the files to the current folder and then delete the empty folder
            if os.path.isdir(path):
                d_files = os.listdir(path)
                for d_file in d_files:
                    filepath = os.path.join(path, d_file)
                    shutil.move(filepath, cur_d)
                shutil.rmtree(path)
            else:
                # get file creation date
                creation_date = os.path.getctime(path)
                creation_date = datetime.datetime.fromtimestamp(creation_date)

                # create a folder named after the creation date if one doesn't already exist and move the file into it
                d_name = creation_date.strftime("%b-%d-%Y")
                destination = os.path.join(cur_d, d_name)
                os.makedirs(destination, exist_ok=True)
                shutil.move(path, destination)

        except Exception as e:
            print(f"Something went wrong. The files could not be organized: {e}")
    
    print("Files were organized.")