#WAP to take some student name form user and store in list....
student=[]
n=int(input("Enter a string range: "))
for i in range(n):
    name=input(f"Enter your name:{i+1} ")
    student.append(name)
    
    
print("Student List Are: ",end="")
for i in student:
    print(i,end=" ")