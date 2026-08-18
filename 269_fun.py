# Variable-Length Arguments :- in which can pass many values
# 1. *args -These are Non-Keyword Arguments  
# 2. **kwargs - These are Keyword Arguments. 


# def display(*data):
#     print(data)

# #main program
# display("ram",34,"indore","obc")


# def add(b,*a):
#     print(b,end=",")
#     sum=0
#     for item in a:
#         sum=sum+item
#     print(sum)    


# add(12,6)    
# add(9,6,10)    
# add(7,6,10,56)   


def dipslay(**d1):
    print(d1)  #{"name":"ram" ,"age":12, "city":"indore"}


dipslay(name="ram",age=12,city="indore")