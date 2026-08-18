# Default argument: 
def display(name,rno,age=0,city="ujjain"): # here default city name is ujjain
    print("student details : ")
    print("name : ",name)
    print("rno : ",rno)
    print("age : ",age)
    print("city : ",city)
    print("------------------")

#main program 
display("shyam",102,city="bhopal", age=30)
display("ram",103,12,"indore")
display("raj",104,50)
display("johan",105,10,"ratlam")
display("anshul",106,30,)
display("aman",107)