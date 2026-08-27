class employee:
    def set_employee(self, name, salary):
        self.name = name
        self.salary = salary

    def emp_display(self):
        print("Employee Details:")
        print("Name:", self.name)
        print("Salary:", self.salary)

class programmer(employee):
    def set_programmer(self, language, project):
        self.language = language
        self.project = project

    def prog_display(self):
        print("Programming Language:", self.language)
        print("Project:", self.project)

programmer1 =  programmer()
programmer1.set_employee("John Doe", 50000)
programmer1.set_programmer("Python", "music player")
programmer1.emp_display()
programmer1.prog_display()   