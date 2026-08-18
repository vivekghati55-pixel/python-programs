class employe():
    def setdata(self,name,id,sallary):  #self is a reference variable which refers to current object 
        self.name=name                   #aapn self ha variable starting gyava ch lagto oops madhe aapn kont pn name deu shkto
        self.id=id
        self.sallary=sallary
        
    def display(self):
        print("Person Info : ")    
        print("name : ",self.name)    
        print("id : ",self.id)    
        print("sallary : ",self.sallary)    
        print("-----------------------------------")    
        

p1=employe()
p1.setdata("Vivek",20,43000)        

p2=employe()
p2.setdata("Badal",20,40000)

p1.display()
p2.display()