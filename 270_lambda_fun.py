#lambda function :- its provide shortest syntext to write small function, lambda function provide one line syntext

# def add(a,b):
#     c= a+b
#     return c

add = lambda a,b : a+b
square = lambda num : num*num

areaOfCircle = lambda radius: 3.141 *radius*radius

display= lambda  : print("hello i am display")
negPos = lambda num : "positive" if num>0 else "nagative"

greater = lambda a,b : a if a>b else b

greater3 = lambda a,b,c : a if a>b and a>c else b if b>c else c

evenNumber =lambda list : [item for item in list if item%2==0]

l1=[1,2,3,4,5,6,7]

print(evenNumber(l1))

l2=[4,7,8,5,9,12,67]

res= evenNumber(l2)
print(res)
# print(greater3(15,457,80))
# print(greater(15,7))
# print(negPos(-5))
# display()
# print(areaOfCircle(4.5))
# print(square(7))
# print(add(12,10))