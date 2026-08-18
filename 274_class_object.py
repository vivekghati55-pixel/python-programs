class car():
    def setdata(self):  #self is a reference variable which refers to current object 
        self.model=input("Enter model :")                   #aapn self ha variable starting gyava ch lagto oops madhe aapn kont pn name deu shkto
        self.year=int(input("Enter year :"))
        self.color=input("Enter color :")
        
    def display(self):
        print("Person Info : ")    
        print("name : ",self.model)    
        print("age : ",self.year)    
        print("village : ",self.color)    
        print("-----------------------------------")    
        

p1=car()
p1.setdata()        

p2=car()
p2.setdata()

p1.display()
p2.display()