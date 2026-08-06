#how to iterate list element..

l1=[15,46,57,90,82]

# print("list element are: ")   #by default \n astech mhanun line change hote
# for ele in l1:
#     print(ele)

print("List Element Are: ",end="")
for ele in l1:
    print(ele,end=" ")
    
    
print("\nsecond way to iterate list element: ")

for i in range(len(l1)):
    print(l1[i])    
    
    
print("Third way to iterate list element: ")
i=0
while i<len(l1):
    print(l1[i])
    i+=1
