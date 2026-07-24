# WAP to check how many vowel in string....
s=input("Enter a String: ")
c=0

for ch in s:
    if ch in "aeiou":
        c+=1
print("string: ",s)
print("Total Vowel In String: ",c)        