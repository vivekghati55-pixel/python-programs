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

class manager(programmer):
    def set_manager(self, team_size, experience):
        self.team_size = team_size
        self.experience = experience

    def mgr_display(self):
        print("Team Size:", self.team_size)
        print("Experience:", self.experience)

manager1 = manager()
manager1.set_employee("Alice Smith", 80000)
manager1.set_programmer("Java", "e-commerce platform")     
manager1.set_manager(10, 5)
manager1.emp_display()  
manager1.prog_display()
manager1.mgr_display()   
