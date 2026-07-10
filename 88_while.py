# WAP to takes a number as input and calculate the sum of its individuals digits...

num=int(input("enter a number : ")) #345
ans=0
while num>0:
    rem=num%10
    ans= ans+rem
    num=num//10
print("sum of individual : ",ans)    