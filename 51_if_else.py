# . Write a program to check whether a character is an alphabet or not.
ch= input("enter a character : ") # A

if ord(ch)>=97 and ord(ch)<=122  or  ord(ch)>=65  and ord(ch)<=90:
    print("char is alphabet")
else:
    print("char is not alphabet")    
