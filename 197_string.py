# WAP to count no of only odd digit in given number...

num=int(input("enter a number: "))
num=str(num)
c=0
for n in num:
    if int(n)%2==1:
        c+=1
print("Odd DIGIT COUNT: ",c)        