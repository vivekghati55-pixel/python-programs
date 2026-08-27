class employee:
    def __init__(self,id,salary,age="no defined"):
        self.id=id
        self.salary=salary
        self.age=age

    def getEmployee(self):
        print("employee info : ")
        print("id :",self.id)  
        print("salary :",self.salary)  
        print("age :",self.age)  
        print("----------------------")
    


e1=employee(101,12000,23)
e2=employee(102,5000)
e3=employee(103,8000)

e1.getEmployee()
e2.getEmployee()
e3.getEmployee()


        