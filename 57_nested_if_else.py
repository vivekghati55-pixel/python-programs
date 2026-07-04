# mini clube entry project
age= int(input("enter your age : "))
if age>=18:
    print("welcome to club : ")
    print("club menue : ")
    print("1. noodles     : 120")
    print("2. sandwitch   : 150 ")
    print("3. cold coffe  : 80 ")
    order=int(input("select item : "))
    if order==1:
        print("your noodles is ordered please pay 120 rs")
    elif order==2:
        print("your sandwitch is ordered please pay 150 rs") 
    elif order==3:
        print("your cold coffe is ordered please pay 80 rs")
    else:
        print("plese select 1,2 or 3")     
else: 
    print("your entry is not allowed")    