def greater(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2   


def sumList(list):
    sum=0
    for item in list:
        sum=sum+item
    return sum    

def length(list):
    c=0
    for item in list:
        c+=1
    return c    



#main program
print(f"greatest num = {greater(34,8)}")

l1=[3,4,5,6,3,6]
print("list : ",l1)
print("list element sum  : ",sumList(l1))

l2=[30,40,50,60,30,60]
print("list : ",l2)
print("list element sum  : ",sumList(l2))
print("list length = ",length(l2))