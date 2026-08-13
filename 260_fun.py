def square():
    num=int(input("enter a num : "))
    res= num*num
    print(f"square of {num} = {res}")


def table():
    num=int(input("enter a num : "))
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")

def greater():
    num1=int(input("enter a num1 : "))
    num2=int(input("enter a num2 : "))
    if num1>num2:
        print("greater num = ",num1)
    else:
        print("greater num = ",num2)    


#main program
# square()    
# table()
greater()