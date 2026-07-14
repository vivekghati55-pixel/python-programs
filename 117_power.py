#Calculate power of a number without using pow(). 
n=int(input("enter a num : "))  #5
p=int(input("enter a power : "))  #3
ans=1
for i in range(p):
    ans=ans*n

print("result = ",ans)
