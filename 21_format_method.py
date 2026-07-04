# print stmnt with format method
name= "vivek ghati"
age = 20
height = 6.1
a=20
b=6
c=a+b
print("my name is {}".format(name))
print("my name age is {} year".format(age))
print("my name height is {} feet".format(height))

print("sum of {} and {} = {}".format(a,b,c))

print("sum of {0} and {0} = {0}".format(a,b,c))

print("sum of {x} and {y} = {z}".format(x=a,y=b,z=c))
