# Write a program to print squares of all numbers present in a given list. 

l1=[]
n=int(input("Enter a number: "))
for i in range(n):
    given=int(input(f"Enter a number: {i+1} "))
    l1.append(given)
    
print("list element are: ",end="")
print(l1,end=" ")

for ele in l1:
    print(f"\nSquare of list element {ele} = {ele*ele} ")