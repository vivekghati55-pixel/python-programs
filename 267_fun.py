# Keyword arguments:- here we pass argument in function with keyword
def display(name,rno,age,city):
    print("student details : ")
    print("name : ",name)
    print("rno : ",rno)
    print("age : ",age)
    print("city : ",city)
    print("------------------")



#main program 
display(city="indore" ,age=12 , rno=101 , name="ram")
display("shyam",102,city="bhopal", age=30)