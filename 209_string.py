# 10.  Write a program to copy one string into another.

s=input("Enter a String: ")
copy=""
for ch in s:
    copy=copy+ch
print("string: ",s)
print("copy string: ",copy)    