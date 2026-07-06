# WAP to display square of 1 to n (given number)

given=int(input("enter ending range"))
num=1
while num<=given:
    print(f"square of {num} = {num*num}")
    # print("square of ",num,"=",num*num)
    num=num+1