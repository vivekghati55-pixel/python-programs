#how to read a binary file
image=open(r'C:\Users\PC\Desktop\Demo\cat.jpg','rb')
data=image.read()
print(data)
image.close()