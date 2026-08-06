# . Write a program to count how many even numbers are present in an list.
l1=[]
n=int(input("Enter a number: "))
for i in range(n):
    num=input(f"Enter a number: {i+1} ")
    l1.append(num)
    
print("list element are: ",end="")
print(l1,end=" ")
c=0
for data in l1:
    if int(data) % 2 == 0:
        c+=1

print(f"\nTotal number of even numbers present in list are: {c}")        
    