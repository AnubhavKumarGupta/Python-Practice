import math as m

n = int(input())
r = int(input())
n1 = n - r
cal = (m.factorial(n)) / (m.factorial(n1) * m.factorial(r))
print(cal)
cal1 = cal % 1000003
print(cal1)
