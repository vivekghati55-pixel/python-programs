#os modules :- make folder, delete folder, get current folder path
# rename file name ,  display file name inside folder

import os 
# its return current working folder path
# path=os.getcwd() :-cwd:corrent working directory..
# print("my path = ",path)

#listdir :- its return a list of file name 
# l1=os.listdir()
# # print(l1)
# for f in l1:
#     print(f)


#its provide file list which contain inside folder
# l1=os.listdir(r'C:\Users\PC\Desktop\rimzim')
# # print(l1)
# for file in l1:
#     print(file)


# mkdir :- its make folder inside computer
# os.mkdir(r'C:\Users\vivek\OneDrive\Desktop\demo\vivek')


#rmdir() :- its delete folder from computer
os.rmdir(r'C:\Users\vivek\OneDrive\Desktop\demo\vivek')


# makedirs:- you can make multiple sub folder
# os.makedirs(r"C:\Users\PC\Desktop\Demo\songs\south song\ramcharn song")

#make 100 folders using loop
# for i in range(100):
#     os.mkdir(f"C:\\Users\\PC\\Desktop\\Demo\\bhajan{i+1}")



# here we delete 100 folders 
# for i in range(100):
#     os.rmdir(f"C:\\Users\\PC\\Desktop\\Demo\\bhajan{i+1}")


# its delete file from computer

# os.remove(f"C:\\Users\\PC\\Desktop\\Demo\\abc.txt")