# file=open(r'C:\Users\PC\Desktop\Demo\ravi.txt','w')
# file.write("hi i am ravi")
# file.close()

# write same with  "with block"
# with block automatically close file 

with open(r'C:\Users\PC\Desktop\Demo\ravi.txt','w') as myfile:
    myfile.write("hi i am Vivek")