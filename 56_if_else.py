# 14. Given a month number, print the number of days (with Feb as 28 days).
month=int(input("enter a month number : ")) #2
if month in [1,3,12,5,10,7,8]:
    print("31 days")
elif month in [11,4,6,9]:
    print("30 days")
elif month==2:
    print("28 days")
else:
    print("invalid month number")        