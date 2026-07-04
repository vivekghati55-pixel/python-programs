# Wap to find greatest number among has given four numbers without using 
# logical and operator.
a= int(input("enter value of a : "))
b= int(input("enter value of b : "))
c= int(input("enter value of c : "))
d= int(input("enter value of d : "))

if a>b:
    if a>c:
        if a > d:
            print("gretest num : ",a)
        else:
            print("gretest num : ",d)
    else:
        if c>d:
            print("gretest num : ",c)
        else:
            print("gretest num : ",d)    
else:
    if b>c :
        if b>d:
            print("gretest num : ",b)
        else:
            print("gretest num : ",d)    
    else:
        if c>d:
            print("gretest num : ",c)
        else:
            print("gretest num : ",d)    
    