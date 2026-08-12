# # Create a set with numbers 1 to 10 and display it. 
# s1=set()

# for i in range(1,11):
#     s1.add(i)
# print(s1)



#  Create a set and print all elements using loop.  
# s1={4,3,6,7,8,9}
# for item in s1:
#     print(item)



#  Check whether an element exists in a set or not. 
# s1={3,6,4,7,8,9,45}
# ele=9
# if ele in s1:
#     print("element is found")
# else:
#     print("element is not found")   



# Find length of a set without using len() (using loop). 
# s1={4,6,3,7,8,55,88}
# # print(len(s1))
# c=0
# for item in s1:
#     c=c+1

# print(f"set : {s1}")
# print("set length : ",c)


# Convert list into set. 
# l1=[3,4,2,2,5,3,6,7]
# print(l1)
# s1= set(l1)
# print(s1)


# Convert string into set and display unique characters.
# s1="hello world institute"

# uniqueChar= set(s1)
# print("string : ",s1)
# print("only unique char : ",end="")
# for char in uniqueChar:
#     print(char,end="")


# Take input from user and store unique values in set. 

# s1=set()
# while True:
#     num=int(input("enter a number : "))
#     s1.add(num)
#     choise=input("you want to add more press y/Y : ") #p
#     if choise != 'y' and choise !='Y' :
#         break

# print("my set : ",s1)


#find union of two list witouth using union method and operator
l1=[1,2,3,4,5]
l2=[4,5,6,7,8]
l3=[]

for item in l1:
    l3.append(item)

#l3=[1,2,3,4,5]

for item in l2:
    if item not in l3:
        l3.append(item)

print(l1)
print(l2)
print(l3)





