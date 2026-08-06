#  Write a program to display the list elements in reverse order. using take user input
    
l1=[]
n=int(input("enter a number: "))
for i in range(n):
    num=int(input(f"Enter a number: {i+1} "))
    l1.append(num)
    
    
print("list element are: ",end="")
print(l1,end=" ")

print("\nlist element reverse",l1[::-1])