#WAP to print theinformation of person using class and object user input..


class person():
    def setdata(self):  #self is a reference variable which refers to current object 
        self.name=input("Enter A Name: ")                  #aapn self ha variable starting gyava ch lagto oops madhe aapn kont pn name deu shkto
        self.age=int(input("Enter A Age:"))
        self.village=input("Enter a village name:")
        
    def display(self):
        print("Person Info : ")    
        print("name : ",self.name)    
        print("age : ",self.age)    
        print("village : ",self.village)    
        print("-----------------------------------")    
        

p1=person()
p1.setdata()        

p2=person()
p2.setdata()

p1.display()
p2.display()