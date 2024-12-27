a = int(input())
even = 0
odd = 0
while a != 0:
    last = a % 10
    if last % 2 == 0:
     even=even + last
    else:
        odd = odd+last
    a = a//10
print(even, " ", odd)
