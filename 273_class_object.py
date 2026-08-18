class car():
    def setdata(self,model,year,color):  #self is a reference variable which refers to current object 
        self.model=model                   #aapn self ha variable starting gyava ch lagto oops madhe aapn kont pn name deu shkto
        self.year=year
        self.color=color
        
    def display(self):
        print("Person Info : ")    
        print("name : ",self.model)    
        print("age : ",self.year)    
        print("village : ",self.color)    
        print("-----------------------------------")    
        

p1=car()
p1.setdata("mercedis",2020,"black")        

p2=car()
p2.setdata("BMW",2021,"White")

p1.display()
p2.display()