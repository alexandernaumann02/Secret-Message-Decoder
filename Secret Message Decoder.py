import os

def rename_files():
    file_list = os.listdir(r"/Users/marknaumann/Desktop/alphabet")

    saved_path = os.getcwd()
    print("Current Working Directory is "+saved_path)
    os.chdir (r"/Users/marknaumann/Desktop/alphabet")

    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)

rename_files()
    
