# WAP to check number is prime or not n (given number).....

num=int(input("Enter a number: "))

for n in range(2,num):
    if num%n==0:
        print("Num is not prime...!!")
        break
else:
    print("num is primee")        