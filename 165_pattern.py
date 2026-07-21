for i in range(1,6): # 1 2 3
    for j in range(1,i+1): # 1 2 3
        if i%2==0:
            print("1",end=" ")
        else:
            print("0",end=" ")    
    print()    