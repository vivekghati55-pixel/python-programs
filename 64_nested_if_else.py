# Write a program to accept roll no and marks of 5 subjects of a student, if 
# individuals  subject have above 40 marks so print student qualify exam 
# otherwise print student fail in exam and if student qualify exam so 
# Calculate  percentage got in exam  by  student. 
# a. If per greater than or equal to 75  A grade 
# b. If per between 60-75  B grade 
# c. If per between 50-60  C grade 
# d. If per between 40-50  D grade 

rno=int(input("enter rno : "))
s1= int(input("enter hindi marks : "))
s2= int(input("enter math marks : "))
s3= int(input("enter science marks : "))
s4= int(input("enter english marks : "))
s5= int(input("enter social science marks : "))

if s1>=40 and s2>=40 and s3>=40 and s4>=40 and s5>=40:
    print("student rno : ",rno)
    print("student qualify exam")
    per = ((s1+s2+s3+s4+s5)/500)*100
    print("percentage : ",per)
    if per>=75 and per<=100:
        print("gread A")
    elif per>=60 and per<75 :
          print("gread B") 
    elif per>=50 and per<60 :
          print("gread C")  
    elif per>=40 and per<50 :
          print("gread D")            
else:
    print("student fail in exam")    