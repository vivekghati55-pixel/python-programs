# function with paramter and with return value
def add(a,b):
    c=a+b
    return c


#main program
print("addition : ",add(12,10))
print("result : ",add(17,10))
print("sum : ",add(5,9))

# ans=add(56,22)
# if ans%2==0:
#     print(f"{ans} is even")
# else:
#      print(f"{ans} is odd")    


# if add(4,7)%2==0:
#     print("res is even")
# else:
#     print("res is odd")    


if add(4,7)%2==0:
    print(f"{add(4,7)} is even")
else:
    print(f"{add(4,7)} is odd")


l1=[45,67,89,9,6]
print(l1[add(1,3)])    