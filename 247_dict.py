# Write a program to create a dictionary of student name and age and print it.

students={}

n=int(input("enter no of student : "))# 5

for i in range(n):
    name=input(f"enter student{i+1} name : ")
    age=int(input("enter age : "))
    students[name]=age


print(students)   # {"ram":12, "shyam":56 , "radha":12}
print("name   age ")
for student in students:
    print(f"{student}   =   {students[student]}")