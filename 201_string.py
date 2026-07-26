# 3. Write a program to find the length of only string alphabet not space a string without using built-in functions.

s=input("Enter a String: ")
l=0
for ch in s:
   if ch>='a' and ch<='z':
        l+=1
print("lengh of string: ",l)    