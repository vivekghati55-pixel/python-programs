x=int(input("enter a num : "))# -8
try:
    if x<0:
       raise ValueError("nagative value error")
except ValueError as e:
    print(e)    
else:
    print("value of x = ",x)
print("program run succefully")