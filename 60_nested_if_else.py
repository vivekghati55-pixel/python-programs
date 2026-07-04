# Check whether a character is a vowel, consonant, or not an alphabet.
ch=input("enter a char : ")
if ch>='a' and ch<='z' or ch>='A' and ch<='Z':
    if ch in "aeiouAEIOU":
        print("char is vovel")
    else:
        print("char is consonent")    

else:
    print("not alphabet")