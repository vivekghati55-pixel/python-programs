# WAP to display multiple of 7 between given range..
num=int(input("enter a start range"))
given=int(input("enter a last range"))
while num<=given:
    if num%7==0:
        print(num,end=" ")
        num=+1