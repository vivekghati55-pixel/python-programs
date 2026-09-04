print("start file reading program...")
try:
    file=open(r"C:\Users\PC\Desktop\Demo\square.txt",'r')
    print(file.read())
except FileNotFoundError as e:
    print(e)  
except AttributeError as e:
    print(e)      
finally:
    file.close()
    print("file close succefully") 

print("all stmnt run succeflly")