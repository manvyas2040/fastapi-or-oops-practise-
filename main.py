from pathlib import Path
import os 
def readfileandfloder():
    path  = Path('')
    items=list(path.rglob('*'))
    for i,items in enumerate(items):
        print(f"{i+1}: {items}")
def creatfile():
    readfileandfloder()
    try:
        name= input("pless tell your file :")
        p =Path(name)
        if not p.exists():
            with open(p,'w') as fs:
                data = input("what you want to write :")    
                fs.write(data)
                print("file created succesfuly....")   
        else:
            print("this file exist") 
    except Exception as err:
        print(f"error acord {err}")
def readfile():
    readfileandfloder()
    try:
        file=input("which file want to read :")
        p=Path(file)
        if p.exists() is p.is_file():
            with open(p,'r') as fs:
                data=fs.read()
                print(data)
                print("readed seccesfuly...")
        else:
            print("file is dosen't exist")
    except Exception as err:
        print(f"an error acord {err}")   
def updetfile():
    readfileandfloder()
    try:
        file=input("which file you want updet : ")
        p=Path(file)
        if p.exists() is p.is_file():
            print("press 1 for changing name file :")
            print("press 2 for overrighting  data file :")
            print("press 3 for appeding some content in file :")
            res =int(input("tell your response : "))
            if res == 1:
                file2=input("tell your new file name :")
                p2=Path(file2)
                p.rename(p2)
            if res ==2 :
                with open (p,'w') as fs :
                    data = input("tell me you want write the data :")
                    fs.write(data)
            if res == 3:
                 with open (p,'a') as fs :
                    data = input("tell me you want append :")
                    fs.write(" "+data)
    except Exception as err:
        print(f" an error ocorde {err}")

def deletefile():
    try:
        readfileandfloder()
        name=input("which file you want to delete :")
        p=Path(name)
    
        if p.exists() and p.is_file():
           os.remove(name)

           print("file remove succesfully")
        else:
            print("no such file exist ")
    except Exception as err:
        print(f"error ocerd by {err}")


print("press creating file 1: ")
print("press reading file 2: ")
print("press updating file 3: ")
print("press deletion file 4: ")

cheak=int(input("enter your respons : "))
if cheak == 1:
    creatfile()
if cheak == 2:
    readfile()
if cheak == 3:
    updetfile()
if cheak == 4:
    deletefile()

