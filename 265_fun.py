#python return multiple result in tuple data type

def operation(num):
    square=num*num
    cube= num*num*num
    return square,cube,"this is random",[4,6,7,8],{"book":89}


# print(operation(4))
res=operation(4)
print(res)
print("square = ",res[0])
print("cube = ",res[1])
print("random = ",res[2])