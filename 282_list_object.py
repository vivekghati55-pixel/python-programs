# object list in python
class student:
    def setStudent(self):
        self.name=input("\nenter your name : ")
        self.rno=int(input("enter rno :"))
        self.per=eval(input("enter percentage :"))

    def getResultCard(self):
        print("student Result Card : ")
        print(f"name = {self.name}")
        print(f"rno = {self.rno}")
        print(f"per = {self.per}%")
        if self.per>=33:
            print("Student Pass")
        else:
            print("Student Fail")    
        print("-----------------")
   

students=[]
n= int(input("enter number of student : ")) # 5
for i in range(n): 
    st= student()
    students.append(st)

for obj in students:
    obj.setStudent()   

for obj in students:
    obj.getResultCard()     




