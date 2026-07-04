# Write a program to check whether a character is an alphabet, digit or special 
# character.
ch= input("enter a character : ") # hello
if ch>='a' and ch<='z'  or ch>='A' and ch<='Z':
    print("char is alphabet")
elif ch>='0' and ch<='9':
    print("char is digit")
else:
    print("special symbole")    
