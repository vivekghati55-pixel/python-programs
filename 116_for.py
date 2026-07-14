# WAP to print num is perfect or not...

given=int(input("Enter a Number: "))
sum=0

for n in range(1,given+1):
    if given%n==0:
        sum=sum+n
if sum==given*2:
    print("num is perfect ") # perfect means example 6 diya 
else:                        # toh factors me 6 chhod ke factors ki sum 6 aayega toh perfect num
    print("num is not perfect")            