print("this is diviosionb apps:")
l1=[12,34,35,56,78,89]
try:
    a=int(input("enter a number:"))
    b=int(input("enter b nymber:"))
    c=a/b
    print("division is :",c)
    index=int(input("enter index number:"))
    print("element at index is :",l1[index])
    
except ZeroDivisionError:
    print("zero division error")

except ValueError:
    print("value error")

except IndexError:
    print("index error")

except :
    print("something went wrong")
    
print("Addition apps:")
a=int(input("enter a number:"))
b=int(input("Enter b number:")) 
c=a+b
print("Addition is ",c)   
print("all code execute successfully")
    
    
               