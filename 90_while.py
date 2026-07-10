# WAP that takes a number as input and counts how many digits its contains...
num=int(input("enter a number : ")) #345
ans=0
while num>0:
    rem=num%10
    ans= ans+1
    num=num//10
print("total digits count in number : ",ans)    