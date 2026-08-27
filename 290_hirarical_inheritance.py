class Student:
    def setStudent(self,name,rno,fees):
      self.name=name
      self.rno=rno
      self.fees=fees
    def getStudent(self):
      print("Student info : ")
      print("name :",self.name)  
      print("rno :",self.rno)  
      print("fees :",self.fees)  


class EngStd(Student):
    def setEngStd(self,branch,sem):
        self.branch=branch
        self.sem=sem
    def getEngStd(self): 
        print("branch :",self.branch) 
        print("sem :",self.sem) 
        print("----------------------")


class MedStd(Student):
    def setMedStd(self,speci,prof):
        self.speci=speci
        self.prof=prof
    def getMedStd(self): 
        print("specialization :",self.speci) 
        print("prof :",self.prof) 
        print("----------------------")

e1=EngStd()
e1.setStudent("Ravi",101,12000)
e1.setEngStd("CSE",5)
e1.getStudent()
e1.getEngStd()


m1=MedStd()
m1.setStudent("Ramesh",102,15000)
m1.setMedStd("Cardiology", 2)
m1.getStudent()
m1.getMedStd() 