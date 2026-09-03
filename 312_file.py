import os

#rename function change file name
# src="C:\\Users\\PC\\Desktop\\Demo\\ram.txt"
# dst="C:\\Users\\PC\\Desktop\\Demo\\shyam.txt"
# os.rename(src,dst)


# # x mode used only create file
# open(r"C:\Users\PC\Desktop\Demo\ram.txt","x")


# remove() :- delete file 
# os.remove(r"C:\Users\PC\Desktop\Demo\ram.txt")


# delete only empty folder
# os.rmdir(r"C:\Users\PC\Desktop\hello")

# os.rmdir(r"C:\Users\PC\Desktop\mydemo")


# import shutil
# shutil.rmtree(r"C:\Users\PC\Desktop\mydemo")

# os.path.exists():- its cheke path  exist or not
# res=os.path.exists(r"C:\Users\PC\Desktop\Demo\shyam.txt")
# print(res)



path=input("enter a path : ")
if os.path.exists(path):
    with open(path) as file:
        r=file.read()
        print(r)
else:
    print("file is not exist")