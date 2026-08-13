# #some methods py
# s1={1,2,3,4}
# s2={3,4,5,6}

# #union:-contain all value both set and duplicate value only once time
# there are two types of union ways:- 1) union() 2) | (bitwise or)
# s3=s1.union(s2)
# s3=s1|s2

# #upadte() :- its also find union but update in one set
# # s1.update(s2)
# # s2.update(s1)
# print(s1)
# print(s2)
# print(s3)



# s1={1,2,3,4}
# s2={3,4,5,6}

# #intersection():- its keep only common values
# # s3= s1.intersection(s2)
# # s3= s1&s2
# # s1.intersection_update(s2)

# print(s1)
# print(s2)
# # print(s3)



# s1={1,2,3,4}
# s2={3,4,5,6}

# #symmetric_difference:- keep unique value only , common value exclude
# # s3=s1.symmetric_difference(s2)
# # s3=s1^s2   # bitwise x-or
# s1.symmetric_difference_update(s2)
# print(s1)
# print(s2)
# # print(s3)


s1={1,2,3,4}
s2={3,4,5,6}
# s3=s1.difference(s2)
# s3=s2.difference(s1)
# s3=s1-s2  
s1.difference_update(s2)
print(s1)
print(s2)
# print(s3)