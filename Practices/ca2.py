# s = "Innovation Facilitation through Cloud Computing:"
# print(s.upper())
n =int(input())
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print("Leap year")
else:
    print("Not leap year")
