#  WAP to print cube of 1 to n (given number)...

given=int(input("Enter a Number: "))

for n in range(1,given+1):
    print(f"Cube of {n}X{n}X{n} = {n*n*n}")