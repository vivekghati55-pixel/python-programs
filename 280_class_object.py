class employe():
    def setdata(self):  #self is a reference variable which refers to current object 
        self.name=input("Enter name : ")                   #aapn self ha variable starting gyava ch lagto oops madhe aapn kont pn name deu shkto
        self.id=input("Enter id : ")
        self.sallary=input("Enter sallary : ")
        
    def display(self):
        print("Person Info : ")    
        print("name : ",self.name)    
        print("id : ",self.id)    
        print("sallary : ",self.sallary)    
        print("-----------------------------------")    
        

p1=employe()
p1.setdata()        

p2=employe()
p2.setdata()

p1.display()
p2.display()