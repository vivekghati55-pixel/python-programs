# WAP to print sum of 1 to n (given number).

given=int(input("enter a number: "))
num=1
res=0
while num<=given:
    res=res+num
    num+=1
print(f"sum of {given} = {res}")
print(f"sum of average {given} = {res/given}")    