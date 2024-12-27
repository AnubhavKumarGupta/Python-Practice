def no_rep(number):
    digits = str(number)
    return len(digits) == len(set(digits))

def with_no_rep(m, n):
    count = 0
    for number in range(m, n + 1):
        if no_rep(number):
            count += 1
    return count

m = 1
n = 20
count = with_no_rep(m, n)
print(count)
