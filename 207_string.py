# 8. Write a program to reverse a string. 
# s=input("Enter a String: ")
# print("string: ",s)
# for ch in s:
#     revrstr=s[::-1]
# print("string reverse: ",revrstr)    

s=input("Enter a String: ")
print("string: ",s) #ram
revrstr=""
for i in range(len(s)-1,-1,-1):
    revrstr=revrstr+s[i] #mar
    
print("string reverse: ",revrstr)   