from pickle import load

text=open(r"C:\Users\vivek\OneDrive\Desktop\demo\adhvika.txt","rb")
l2=load(text)
print(l2)
text.close()