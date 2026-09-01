fruits=["apple\n","banana\n","mango\n","orange\n","grapus\n"]
file=open(r"C:\Users\PC\Desktop\Demo\data.txt",'w')
# for fruit in fruits:
#     file.write(fruit)

# write lines is used to list in file but list must contain string data
file.writelines(fruits)

file.close()