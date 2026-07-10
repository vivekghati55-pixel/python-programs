# write a program taken a number as input and prints rach digit of the
# number in reverse order, with each digit displayed on a seperate line.
num=int(input("enter a number : "))
while num>0:
    res=num%10
    print(res)
    num=num//10
