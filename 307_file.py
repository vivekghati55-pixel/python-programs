# read data from file
# file= open(r'C:\Users\PC\Desktop\Demo\square.txt','r')
# # read() :- its read data from file
# data = file.read()
# print(data)
# file.close()



# file= open(r'C:\Users\PC\Desktop\Demo\square.txt','r')
# # read(5) :- its read only 5 character
# data = file.read(5)
# print(data)
# file.close()


# file= open(r'C:\Users\PC\Desktop\Demo\square.txt','r')
# # readline():- its read only one line
# data = file.readline()
# print(data)

# data = file.readline()
# print(data)

# data = file.readline()
# print(data)

# file.close()




# file= open(r'C:\Users\PC\Desktop\Demo\square.txt','r')
# # readlines():- its read only all lines and return a list
# l1=file.readlines()
# print(l1)
# file.close()


file= open(r'C:\Users\PC\Desktop\Demo\square.txt','r')
# readlines():- its read only all lines and return a list
l1=file.readlines()
for line in l1:
    print(line,end="")
file.close()