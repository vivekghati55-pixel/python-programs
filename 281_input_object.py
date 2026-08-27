# object input take form user
class student:
    def setStudent(self):
        self.name=input("enter your name : ")
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
   

s1= student()
s1.setStudent()

s2=student()
s2.setStudent()

s3=student()
s3.setStudent()

s1.getResultCard()
s2.getResultCard()
s3.getResultCard()

