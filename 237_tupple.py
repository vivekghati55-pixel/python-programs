#how to change tuple
# frist convert in list then change and again convert in tuple
t1=(4,5,3,6,7,8,9,2,3,12)
print(type(t1))
print(t1)

l1= list(t1)   # convert in list
print(type(l1))
l1.append(500)  # chnage in list
t1= tuple(l1)    # again convert in tuple
  
print(t1)