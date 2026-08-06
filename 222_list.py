#WAP to take input and print all element of list...
l1=[]
n=int(input("enter a list range: "))
for i in range(n):
    num=int(input(f"enter anumber:{i+1} "))
    l1.append(num)

print("list elements are: ",end="")
for i in l1:
    print(i,end=" ")