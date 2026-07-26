# 13.  Write a program to find the frequency of each character in a string.
# banana
#a=3
#b=1
#n=2

s=input("Enter a String: ")#banana
freq={}
for ch in s:
    if ch != " ":
        if ch in freq: #punha punha letter asl tr ek ek ne count vadhavtoy
            freq[ch]+=1
        else:
            freq[ch] =1 #pahilyandach bhetla letter tr tyachi values one asignn karto
print("character Frequency: ")  
for ch,count in freq.items():
    print(ch,"=",count)             
        