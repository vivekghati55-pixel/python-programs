# List Comprehension: List Comprehension offers the shortest syntax for looping through lists.
# its mostaly used to make a new list with existing list.

#wap to make a new list which containe square of given list.

# l1=[3,2,4,5,6,7]
# l2=[]
# for ele in l1:
#     square= ele*ele
#     l2.append(square)

# print("input list : ",l1)      
# print("square list : ",l2)    


#same question by using list comprehension

# l1=[3,2,4,5,6,7]
# l2=[ele*ele for ele in l1]
# print("input list : ",l1)      
# print("square list : ",l2) 



# l1=[3,2,4,5,6,7]
# l2=[ele*+5 for ele in l1]
# print("input list : ",l1)      
# print("square list : ",l2) 


# l1=[3,2,4,5,6,7]
# l2=[ele*ele*ele for ele in l1]
# print("input list : ",l1)      
# print("square list : ",l2) 
     

# you wnat to make a normal list which containe 1 to number
# l1=[n for n in range(1,11)]
# print(l1)


#using list comprehension filter on existing list

# l1=[2,5,4,6,7,8,9,1]

# l2=[]
# for ele in l1:
#     if ele%2==0:
#         l2.append(ele)

# print("input list : ",l1)        
# print("even list : ",l2)     


# l1=[2,5,4,6,7,8,9,1]
# l2=[ele for ele in l1 if ele%2==0]
# print("input list : ",l1)        
# print("output list : ",l2)   


# l1=[2,5,4,6,7,8,9,1]
# l2=[ele for ele in l1 if ele%4==0]
# print("input list : ",l1)        
# print("output list : ",l2)   


# l1=[2,5,4,6,7,8,9,1]
# l2=[ele*ele for ele in l1 if ele%2==0]
# print("input list : ",l1)        
# print("output list : ",l2)   


# l1=[42,546,67,5,675,23412]
# l2=[ele for ele in l1 if len(str(ele))==3]
# print("input list : ",l1)        
# print("output list : ",l2)   


# l1=["apple","mango","papaya","watermelon"]
# l2=[ele for ele in l1 if "m" in ele]
# print("input list : ",l1)        
# print("output list : ",l2)   


l1=[42,546,67,5,100,675,23412,223]
l2=[ele for ele in l1 if ele>50 and ele<500]
print("input list : ",l1)        
print("output list : ",l2)   