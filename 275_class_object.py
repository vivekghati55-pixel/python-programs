class mouse():
    def setMouse(s,com,col,rat,p):
        s.company=com
        s.color=col
        s.rating=rat
        s.price=p

    def getMouse(obj):
        print("mouse info :") 
        print("company :",obj.company)
        print("color :",obj.color)
        print("rating :",obj.rating)
        print("price :",obj.price)
        print("---------------------")


m1=mouse()
m1.setMouse("HP","black",4.5,600)

m2= mouse()
m2.setMouse("Fronttech","red",2.4,400)

m1.getMouse()
m2.getMouse()





