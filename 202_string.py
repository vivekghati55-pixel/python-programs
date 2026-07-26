# 4. Write a program to count the number of vowels and consonants in a string. 

s=input("Enter a String: ")
VowelCount=0
ConsCount=0
for ch in s:
  if ch>='a' and ch<='z':    #<--space count nhi krt space asli tr loop chalt ch nhi jr count 
    if ch in 'aeiou':        # kraychi asel tr varchi line commend kra....  
        VowelCount+=1
    else:
        ConsCount=ConsCount+1

print("Vowel Counts: ",VowelCount)
print("Consonent Counts: ",ConsCount)        