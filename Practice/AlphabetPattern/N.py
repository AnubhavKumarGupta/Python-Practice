for row in range(7): # 0 to 6   
    for col in range(5): # 0 to 4   
        if (row!=2 and row!=3 and row!=4) and (col==0 or col==4):   
            print('*',end=' ')   
        elif (row==2) and (col!=2 and col!=3):   
            print('*',end=' ')   
        elif (row==3) and (col%2==0):   
            print('*',end=' ')   
        elif (row==4) and (col!=1 and col!=2):   
            print('*',end=' ')   
        else:   
            print(' ',end=' ')   
    print()  