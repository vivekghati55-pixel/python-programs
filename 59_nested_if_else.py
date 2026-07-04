# Write a program to read the age of a candidate and determine whether he 
# is eligible to cast his/her own vote in india or not.
country = input("enter your country : ")
if country=="india":
    age= int(input("enter your age : "))
    if age>=18:
        print("you can vote in india")
    else:
        print("you are not eligible for voting")
else:
    print("you are not indian")