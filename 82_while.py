# WAP to print sum 1 to n (given number) only even number sum.

given=int(input("enter a number: "))
num=1
res=0
while num<=given:
    if num%2==0:
        res=res+num
    num+=1
print(f"sum of 1 to {given} even number = {res}")        