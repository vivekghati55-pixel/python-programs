#WAP to find the sum of all elements in an list...
l1=[]
n=int(input("Enter a number: "))
for i in range(n):
    num=int(input(f"enter a number: {i+1}"))
    l1.append(num)
    
print("list elments are: ")
print(l1)
sum=0

for ele in l1:
    sum=sum+ele # 13

print("sum of list element is = ",sum)
print("average of list element is = ",sum/len(l1))

if sum%2==0:
    print("sum is even")
else:
    print("sum is odd")    