print("this is division app :")
try: 
  a=int((input("enter a : "))) #"hello"
  b=int((input("enter b : ")))  # 0
  c=a/b
except ZeroDivisionError as e:
  print(e) 
except ValueError as e: 
  print(e)
except:
  print("something is wrong")    
else:
  print("division =  %.2f"%c)
  print("else exicute")  
print("division program run succefully")