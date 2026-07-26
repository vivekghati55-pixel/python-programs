# 8. Write a program to reverse a string. 

s=input("Enter a String: ")
print("string: ",s)
revrstr=""

for ch in s:
    revrstr=ch+revrstr
print("string reverse: ",revrstr)    