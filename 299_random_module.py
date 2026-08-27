import random

#randint() :- its provode random integer value from given range
# num=random.randint(1,10)
# print(num)

#random():- its provide random value between 0 to 1
# num=int((random.random())*100)
# print(num)


# choice() :- its provide random value from given sequence 
# l1=["rock","paper","scissor"]
# res = random.choice(l1)
# print(res)

l1=[34,56,78,90,22]
res = random.choices(l1,k=3)
print(res)