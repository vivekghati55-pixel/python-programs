# copy image from demo folder to my demo folder
image=open(r'C:\Users\PC\Desktop\Demo\cat.jpg','rb')
data=image.read()
image.close()

image=open(r'C:\Users\PC\Desktop\Demo\mycat.jpg','wb')
image.write(data)
image.close()

print("copy image succefully")