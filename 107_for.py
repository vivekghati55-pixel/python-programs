#  WAP to print number square 1 to n (given number)...

given=int(input("Enter a number: "))

for n in range(1,given+1):
    print(f"suare of {n} x {n} = {n*n}")