# split():-its seperate all world of string and create a list then return list...
# split():- aapn ek line madhil sentence, sentence madhil per words different vr print krnya sathi krto...
# s="Adhvika his my niece its a very beauty girl"   
# l1=s.split()              
# print(s)
# for word in l1:
#     print("split using string: ",word)


#WAP to print how many character present in string each word...
# s="Badal his my brother currently pursuing forensic last year"   
# l1=s.split()              
# print(s)
# for word in l1:
#     print(f"{word} = {len(word)}")

#WAP to reverse each word in string.....
s="Nagpur is a orange city"
#rupgan si a egnaro ytic
rev=""
l1=s.split()              
print(s)
for word in l1:
    rev=rev+word[::-1]+" "
print(rev)    

# for i in range (len(l1)-1,-1,-1):  # 4 3 2 1 0
#       print(l1[i],end=" ")
         

#  Nagpur is a orange city
n=""
for w in l1:
    n=w+" "+n
print(n)    
    