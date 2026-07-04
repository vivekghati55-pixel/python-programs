#write program to print state full name according to short name
shortState= input("enter state short name : ")# 
match shortState:
    case "mp":
        print("madhya-pradesh")
    case "up":
        print("utter - pradesh")  
    case "rj":
        print("rajsthan")
    case "mh":
        print("maharashtra") 
    case _:
        print("not valid name")


