class employee:
    # def __init__(self):
    #     self.id=101
    #     self.salary=15000
    #     self.age=25
    def __init__(self):
        self.id=int(input("enter id : "))
        self.salary=eval(input("enter salary : "))
        self.age=eval(input("enter age : "))

    def getEmployee(self):
        print("employee info : ")
        print("id :",self.id)  
        print("salary :",self.salary)  
        print("age :",self.age)  
        print("----------------------")
    


e1=employee()
e2=employee()
e3=employee()

e1.getEmployee()
e2.getEmployee()
e3.getEmployee()


        