def square(num):
    res=num*num
    return res

def sq_range(s,e):
    for i in range(s,e+1): # 0 1
        print(f"square of {i} = {square(i)} ")


#main program
sq_range(1,5)
print("-------------------------")
sq_range(11,15)
print("-------------------------")
sq_range(21,25)


# for i in range(1,6): # 0 1
#     print(f"square of {i} = {square(i)} ")
# print("-------------------------")
# for i in range(11,16): # 0 1
#     print(f"square of {i} = {square(i)} ")    
# print("-------------------------")
# for i in range(21,26): # 0 1
#     print(f"square of {i} = {square(i)} ") 