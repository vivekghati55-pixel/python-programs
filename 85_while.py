# WAP to display factors count of given number..
given=int(input("enter a number : "))
num=1
c=0
while num<=given:
    if given%num==0:
        c+=1
    num+=1    
print("factor count of : ",c)    