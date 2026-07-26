# 9.  Write a program to check whether a string is a palindrome or not.
# palindrome means:- name ahe te ult jri bollo tri tsch aal tr palindrome
# naman
# madam
# malayalam
# mom

s=input("Enter a String: ")
revstr=""

for ch in s:
    revstr=ch+revstr
    
if s==revstr:
    print("string is palindrome") 
else:
    print("string is not a palindrome")       