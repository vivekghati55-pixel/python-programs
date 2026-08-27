class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def emp_display(self):
        print("Employee Details:")
        print("Name:", self.name)
        print("Salary:", self.salary)

class programmer(employee):
    def __init__(self,name,salary, language, project):
        super().__init__(name,salary)
        self.language = language
        self.project = project

    def prog_display(self):
        super().emp_display()
        print("Programming Language:", self.language)
        print("Project:", self.project)

programmer1 =  programmer("John Doe", 50000,"Python", "music player")
programmer1.prog_display()   