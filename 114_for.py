# WAP to print 1 to n (given number)...
# 12--> 1,2,3,4,6,12..
# 15--> 1,3,5,15.....

given=int(input("Enter a number: "))
print(f"factors of {given}= ",end="")
for n in range(1,given+1):
    if given%n==0:
        print(n,end=" ")