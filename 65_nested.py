# Write a Program to accept user’s marital status, gender and age to check if 
# he/she is eligible for marriage or not. 

status= input("enter your marital status 'single' or 'marriage' : ")
if status=="single":
    gender=input("enter your gender 'male' or 'female' : ")
    if gender=="male":
        age= int(input("enter your age : "))
        if age>=21:
            print("you are eligible for marriage")
        else:
             print("you are not eligible for marriage")    
    elif gender=="female":
        age= int(input("enter your age : "))
        if age>=18:
            print("you are eligible for marriage")
        else:
             print("you are not eligible for marriage")   
    else:
        print("please enter male or female")
elif status=="marriage":
    print("you already marriade")
else:
    print("please enter single or marriage ")



    