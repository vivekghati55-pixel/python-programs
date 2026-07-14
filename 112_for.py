# WAP to print sum of 1 to n (given number)...

given=int(input("enter a num: "))
sum=0
for n in range(1,given+1):  #12:-  1+2+3+4+5+6+7+8+9+10+11+12=78  78//12
    sum=sum+n
    
print(f"sum of {given} = {sum} ")
print(f"average of {sum} = {sum/given}")    