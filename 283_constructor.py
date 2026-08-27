class demo: 
    def __init__(self):     # non parameterized constructor
        print("hello i am constructor")

    def __init__(self,a,b):   # parameterized constructor
        print("a = ",a)
        print("b = ",b)
        print("hello 2 para constructor is called")
    
    def display(self):
        print("hello i am display")

d1 = demo(12,45)


