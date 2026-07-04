# Write a program to find greatest number among has given three numbers. 
a= int(input("enter value of a : "))
b= int(input("enter value of b : "))
c= int(input("enter value of c : "))
# a=100 b =670 c= 90
if a>b and a>c :
    print("greatest num : ",a)
elif b>c:
    print("greatest num : ",b) 
else:
    print("greatest num : ",c)     