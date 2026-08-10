#  Write a program to merge two dictionaries. 
d1= {"ram":12, "shyam":56 , "radha":52}
d2= {"book":50, "pen":7 , "pencil":4}
d3={}

for ele in d1:
    d3[ele]= d1[ele]

for ele in d2:
    d3[ele]= d2[ele]

print(d1)
print(d2)
print(d3)


# Write a program to copy one dictionary into another dictionary. 
# d1= {"ram":12, "shyam":56 , "radha":52}
# d2=d1.copy()
# print(d1)
# print(d2)

# second method to copy one dictionary into another dictionary.
# d2={}

# for ele in d1:
#     d2[ele]= d1[ele]

# print(d1)
# print(d2)



#  Write a program to clear all elements of a dictionary. 

# d1= {"ram":12, "shyam":56 , "radha":12}
# # d1.clear()
# l=len(d1)

# for i in range(l):
#     d1.popitem()

# print(d1)




#  Write a program to count total number of key-value pairs in dictionary. 
# d1= {"ram":12, "shyam":56 , "radha":12}

# c=0
# for i in d1:
#     c+=1

# print("total key-paire = ",c)

# . Write a program to check whether a value exists in dictionary or not.
# d1= {"ram":12, "shyam":56 , "radha":12}

# value = 56

# if value in d1.values():
#     print("exist")
# else:
#     print("not exist")    


# for i in d1:
#     if value == d1[i]:
#         print("exit")
#         break
# else:
#     print("not exist")    
     








# Write a program to check whether a key exists in dictionary or not. 
# d1= {"ram":12, "shyam":56 , "radha":12}

# key = "shyam"

# if key in d1:
#     print("exist ")
# else:
#     print("not exist")    