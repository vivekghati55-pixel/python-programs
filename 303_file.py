# how to create file and write data inside file
# its open a file if file exist or if not exist so its create and open

# w mode :- its open file and delete previous data
file = open("C:\\Users\\PC\\Desktop\\Demo\\vivek.txt","w")
file.write("hello this is me\n")
file.write("my name is Vivek Ghati\n")
file.close()