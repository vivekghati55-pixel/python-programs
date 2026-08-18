class student:
    def setStudent(self,name,rno,per):
        self.name=name
        self.rno=rno
        self.per=per

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
s1.setStudent("ram",101,67.89)

s2=student()
s2.setStudent("shyam",102,88.45)

s3=student()
s3.setStudent("raman",103,20.45)

s1.getResultCard()
s2.getResultCard()
s3.getResultCard()

