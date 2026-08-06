# Write a program to display all even numbers present in an list.
l1=[]
n=int(input("Enter a range of list: "))
for i in range(n):
    num=int(input(f"enter a number: {i+1}"))
    l1.append(num)
     
print("list elements are: ")
print(l1)

print("Even numbers present in list are:  ",end="") 
for ele in l1:
    if ele%2==0:
        print(ele,end=" ")    