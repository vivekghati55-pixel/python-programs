# 4. Write a program to make simple calculator. 
#       Press 1 to addition 
#       Press 2 to subtraction 
#       Press 3 to multiplication 
#       Press 4 to division

print("<---welcome to my calculator----> ")
print("    press 1 to addition : ")
print("    press 2 to subtraction : ")
print("    press 3 to multiplication : ")
print("    press 4 to division : ")
num = int(input("press any number : "))

match num:
    case 1:
        a=int(input("enter a value : ")) #7
        b=int(input("enter b value : ")) #9
        c=a+b
        print("addition = ",c)
    case 2:
        a=int(input("enter a value : ")) #7
        b=int(input("enter b value : ")) #9
        c=a-b
        print("subtraction = ",c)    
    case 3:
        a=int(input("enter a value : ")) #7
        b=int(input("enter b value : ")) #9
        c=a*b
        print("multiplication = ",c)            
    case 4:
        a=int(input("enter a value : ")) #7
        b=int(input("enter b value : ")) #9
        c=a/b
        print("division = ",c)       
    case _:
        print("invalid choise")         