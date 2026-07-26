# 7. Write a program to convert a string to lowercase.
#RAM-->ram
# VIVEK-->vivek


s=input("Enter a String: ")
upper=""
for ch in s:
    if ch>='A' and ch<='Z':
        upper=upper + chr(ord(ch)+32)
    else:
        upper=upper+ch

print("upper case: ",upper)            
            