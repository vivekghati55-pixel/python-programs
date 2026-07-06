# WAP to print even number series..

given=int(input("enter a number"))
num=1
while num<=given:
    if num%2==0:
        print(num,end=" ")
        num=num+1