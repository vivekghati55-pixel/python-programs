#set methods
s1={1,2,3,4,5,6}
s2={1,2,3,4}

# if s1.issubset(s2):
#     print("yes s1 is subset of s2")
# else:
#     print("s1 is not subset of s2")    

# if s2.issuperset(s1):
#     print("yes s2 is superset of s1")
# else:
#     print("s2 is not superset of s1")  


#isdisjoint() :- return true if not intersection 
# return false is have intersection

s1={1,2,3,4}
s2={4,5,6,7,8}
print(s1.isdisjoint(s2))