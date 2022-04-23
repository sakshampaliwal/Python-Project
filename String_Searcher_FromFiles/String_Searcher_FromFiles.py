import os

text = input("Please Enter Input Text : ")
path = input("Enter path of the folder : ")

def getfiles(path):
    f = 0
    os.chdir(path)
    files = os.listdir()
    for file_name in files:
        abs_path = os.path.abspath(file_name)
        if os.path.isdir(abs_path):
            getfiles(abs_path)
        if os.path.isfile(abs_path):
            file = open(file_name, "r")
            if text in file.read():
                f=1
                print(text + " found in ")
                final_path = os.path.abspath(file_name)
                print(final_path)
                return True

    if (f == 0):
            print(text + " not found! ")
            return False

getfiles(path)