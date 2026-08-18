class person():
    def setdata(self,name,age,village):  #self is a reference variable which refers to current object 
        self.name=name                   #aapn self ha variable starting gyava ch lagto oops madhe aapn kont pn name deu shkto
        self.age=age
        self.village=village
        
    def display(self):
        print("Person Info : ")    
        print("name : ",self.name)    
        print("age : ",self.age)    
        print("village : ",self.village)    
        print("-----------------------------------")    
        

p1=person()
p1.setdata("Vivek",20,"Ashti")        

p2=person()
p2.setdata("Badal",20,"Amravati")

p1.display()
p2.display()