    # Method - 1 

# import math as m 
# n = int(input())
# print(m.factorial(n))

#########################################

    #Method - 2
    
    
# n = int(input())

# def fact(n):
#     if n in [0,1]:
#         return n
#     else:
#         return n*fact(n-1)
    
# print(fact(n))


##########################################

    # Method - 3
    
n = int(input())

m = 1
for i in range(1,n+1):
    m = m * i
    
print(m)