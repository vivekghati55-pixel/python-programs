# Wap to find greatest number among has given three numbers without 
# using logical and operator.
a= int(input("enter value of a : "))
b= int(input("enter value of b : "))
c= int(input("enter value of c : "))

if a>b:
    if a>c:
       print("greatest num : ",a)
    else:
       print("greatest num : ",c)  
else:
    if b>c:
        print("greatest num : ",b)
    else:
        print("greatest num : ",c)          
    