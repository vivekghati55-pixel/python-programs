# 6. Write a program to convert a string to uppercase.
# ram-->RAM
# vivek-->VIVEK


s=input("Enter a String: ")
upper=""
for ch in s:
    if ch>='a' and ch<='z':
        upper=upper + chr(ord(ch)-32)
    else:
        upper=upper+ch #jr input dila tr input sathi varchi condition false 
                       # mhanun number pn print zhale pahije mhanun else dila..

print("upper case: ",upper)            
            