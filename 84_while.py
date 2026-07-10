# wAP to print factors of given number...
given=int(input("enter a number : "))
num=1
print(f"factors of {given} : ",end="") 
while num<=given:
    if given%num==0:
        print(num,end=" ")
        num+=1   