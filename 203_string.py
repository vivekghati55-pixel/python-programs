# 5. Write a program to count the number of words in a string.

s=input("Enter a String: ")
Wcount=0
for ch in s:
    if ch==" ":
        Wcount+=1
print(f"total no of word = {Wcount+1}")    