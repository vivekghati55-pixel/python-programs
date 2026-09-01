num=int(input("enter a num : "))
square=num*num
print(f"sqare of {num} = {num*num}")
f=open("C:\\Users\\PC\\Desktop\\Demo\\square.txt","a")
f.write(f"sqare of {num} = {num*num}\n")
f.close()