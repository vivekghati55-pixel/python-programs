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

class manager:
    def set_manager(self, team_size, experience):
        self.team_size = team_size
        self.experience = experience

    def mgr_display(self):
        print("Team Size:", self.team_size)
        print("Experience:", self.experience)

class programmer_manager(programmer, manager):
    def set_programmer_manager(self,no_of_projects):
        self.no_of_projects = no_of_projects
    def pm_display(self):
        print("Number of Projects:", self.no_of_projects)    
       

pm1 = programmer_manager()
pm1.set_employee("Bob Johnson", 90000)
pm1.set_programmer("C++", "game development")
pm1.set_manager(5, 7)
pm1.set_programmer_manager(3)       
pm1.emp_display()
pm1.prog_display()
pm1.mgr_display()
pm1.pm_display()