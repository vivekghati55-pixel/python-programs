# WAP top print to display table of given number,
# 6x1= 6 
# 6x2= 12
# 6x3= 18
given=int(input("enter a number"))
num=1
while num<=10:
    print(f"{given}x{num} = {given*num}")
    num=num+1