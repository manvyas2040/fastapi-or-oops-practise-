# from pathlib import Path
# import os
# def readfileandfolder():
#     path=Path('')
#     items=list(path.rglob('*'))
#     for i , items in enumerate(items):
#         print(f"{i+1} : {items}")
# def creatingfile():
    # try:
    #     readfileandfolder()
    #     name=input("pless tell your file name :")
    #     p=Path(name)
    #     if not p.exists() :
    #         with open (p,'w') as fs:
    #             data=input("what you write any conten :")
    #             fs.write(data)
    #         print("file sucessfuly created......")
    #     else:
    #         print("file alredy exist...")
    # except Exception as error:
    #     print(f"error ocuerd by {error}")
# def readingfile():
#     readfileandfolder()
#     try :
#         name=input("which file read you :")
#         p =Path(name)
#         if  p.exists() and p.is_file():
#             with open (p,'r') as fs:
#                 data =fs.read()
#                 print(f"\n{data}\n")
#                 print("file sucessfuly read ...")
#         else:
#             print("file dosen't exists ")
#     except Exception as eror:
#         print(f"error ocuerd by {eror}")
# def updetingfile():
#     readfileandfolder()
#     try :
#         name =input("which file you want to updeat :")
#         p=Path(name)
#         if p.exists() :
#             print("press 1 for changing name file ")
#             print("press 2 for overrighting  data file ")
#             print("press 3 for appeding some content in file ")
#             res = int(input("enter your response :"))
#             if res == 1:
#                 file2=input("enter your new file name :")
#                 p2=Path(file2)
#                 p.rename(p2)
#                 if res == 2:
#                     with open (p,'w') as fs:
#                         data=input("tell me write your data : ")
#                         fs.write(data)
#                 if res == 3:
#                     with open (p,'a') as fs :
#                         data =input("tell me what data you apend :")
#                         fs.write(" "+data)
#     except Exception as error :
#         print(f"error ocerd by {error}")
# def deletfile():
#     try:
#       readfileandfolder()
#       name=input("enter your file name :")
#       p=Path(name)
#       if p.exists():
#           os.remove(name)
#       else:
#           print("file dosen't exists ")
#     except Exception as error:
#         print(f"error ocerd by {error}")  



# print("press 1 for creating file  ")
# print("press 2 for reading  file  ")
# print("press 3 for updating file  ")
# print("press 4 for deleat   file  ")

# cheak=int(input("enter a your choies number :"))
# if cheak == 1:
#     creatingfile()
# if cheak == 2:
#     readingfile()
# if cheak == 3:
#     updetingfile()
# if cheak == 4:
#     deletfile()

from pathlib import Path

def readfileandfloder():
    path =Path('')
    items = list(path.rglob('*'))
    for i ,items in enumerate(items):
        print(f"{i+1} : {items}")
def creatingfile():
    try:

        readfileandfloder()
        name=input("pless tell me your file name: ")
        p=Path(name)
        if not p.exists():
            with open (p,'w') as fn:
                data=input("enter  you file name :")
                fn.write(data)
                print("file sucessfuly created..")
        else :
               print("file alredy exist..")
    except Exception as error:
        print(f"error ocuerd by{error}")
def readingfile():
    try:
        readfileandfloder()
        name=input("enter your file name :")
        p=Path(name)
        if not p.exists():
            with open (p,'r') as fs:
                data=fs.read()
                print(f"/n{data}/n")
                print("file data read successfily...")
        else:
            print("file does not exist...")
    except Exception as error:
        print(f"errorocuerd by {error} ")





print("press 1 for creating file  ")
print("press 2 for reading  file  ")
print("press 3 for updating file  ")
print("press 4 for deleat   file  ")

cheak=int(input("enter a your choies number :"))
if cheak == 1:
    creatingfile()
if cheak == 2:
    readingfile()