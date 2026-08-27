class employee:
    def set_employee(self, name, salary):
        self.name = name
        self.salary = salary

    def emp_display(self):
        print("Employee Details:")
        print("Name:", self.name)
        print("Salary:", self.salary)

class programmer(employee):
    def set_programmer(self,name,salary, language, project):
        super().set_employee(name, salary)
        self.language = language
        self.project = project

    def prog_display(self):
        # self.emp_display()
        # employee.emp_display(self)
        super().emp_display()
        print("Programming Language:", self.language)
        print("Project:", self.project)

programmer1 =  programmer()
programmer1.set_programmer("John Doe", 50000,"Python", "music player")
programmer1.prog_display()   