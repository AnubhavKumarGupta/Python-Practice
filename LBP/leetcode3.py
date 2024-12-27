x = int(input())

def sumOfTheDigitsOfHarshadNumber(x):
    count = 0
    while x != 0:
        d = x % 10
        count = count + d
        x = x // 10
            
    if x % count == 0:
        return count
    else:
        return -1
            
            
            
print(sumOfTheDigitsOfHarshadNumber(x))