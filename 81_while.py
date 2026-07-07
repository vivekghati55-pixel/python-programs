# WAP to display sum of 1 to n (given number).

given=int(input("enter a num: "))
num=1
res=0
while num<=given:
    res=res+num
    if num==given:
        print(num,end="")
    else:
        print(num,end=" + ")
    num+=1
print(" = ",res)                    