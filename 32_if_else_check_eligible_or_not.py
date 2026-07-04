print("check whether you are eligible for vote or not")
num=int(input("enter you age :"))
if num>18 :
    print("you are eligible for vote")
    print("you are eligible for drive the vehicle")
else :
    print("you are not eligible for vote")
    print("are you eligible after =",-(num-18))        
