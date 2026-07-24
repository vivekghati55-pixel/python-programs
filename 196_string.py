# WAP to count no of only even gidit in given number...

num=int(input("enter a number: "))
num=str(num)
c=0
for n in num:
    if int(n)%2==0:
        c+=1
print("EVEN DIGIT COUNT: ",c)        