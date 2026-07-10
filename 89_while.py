# WAP to that takes a number as input and calculates the sum of 
# only  its n um even number...

num=int(input("enter a number : ")) #345
ans=0
while num>0:
    rem=num%10
    if rem%2==0:
        ans= ans+rem 
    num=num//10
print("sum of even individual digits : ",ans)    