import pickle

l1=[12,34,56,78,89]
text=open(r"C:\Users\vivek\OneDrive\Desktop\demo\adhvika.txt","wb")
pickle.dump(l1,text)
for i in l1:
    print(i)
text.close()