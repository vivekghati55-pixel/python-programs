# function with parameter
def add(a,b):     # here 2 parameter a and b 
    c=a+b
    print("addition : ",c)

def square(num):
    res=num*num
    print(f"square of {num} = {res}")

def greater(num1,num2):
    if num1>num2:
        print("greater num = ",num1)
    else:
        print("greater num = ",num2)    


def table(num):
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")

#main program
table(4)
greater(12,90)
greater(120,90)
add(3,5)   
add(10,30)
add(12,6)

square(5)
square(7)