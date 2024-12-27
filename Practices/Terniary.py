# a = int(input("Input the First Number "))
# b = int(input("Input the Second Number "))
# c = a if a > b else b
# print("the max number is ", c)


a = int(input("Input the First Number "))
b = int(input("Input the Second Number "))
c = int(input("Input the third Number "))
d = a if a > b and a > c else b if b > c else c
print("the max number among is ", d)
