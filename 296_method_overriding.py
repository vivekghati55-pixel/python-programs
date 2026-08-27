class A:
    def display(self):
        print("A class display")



class B(A):
    def display(self):
        print("B class display")
        super().display()

b1=B()
b1.display()