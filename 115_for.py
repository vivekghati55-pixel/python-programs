# WAP to check given number is prime or not....

given=int(input("Enter a Number: "))

c=0
for num in range(1,given+1):
    if given%num==0:
        c=c+1
if c==2:
     print("Number is Prime...!!")
     print("~Vivekkk!!")
else:
     print("Number is Not Prime...!!")        