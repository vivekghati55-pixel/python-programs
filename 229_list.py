# . Write a program to copy elements from one list to another.
l1=[12,34,56,78,90]

# l2=l1   #its just copy reference/address not make new list inside memory



# l2=[]
# for ele in l1:
#     l2.append(ele)



l2=l1.copy()

# l2=list(l1)

print(l1)
print(l2) 

l2[2]=60

print(l1)
print(l2)

