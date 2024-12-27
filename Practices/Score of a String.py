# s = "hello"

# n= len(s)
# l = []

# for i in range(n):
#     l.append(ord(s[i]))
    
    
# print(l)

# l2 = []

# le = len(l2)
# f = 0

# for i in range(len(l)):
#     f = f + (abs(l[i] - l[i - 1]))
    
# print(f)


def score_of_string(s):
    score = 0
    for i in range(1, len(s)):
        diff = abs(ord(s[i]) - ord(s[i - 1]))
        score += diff
    return score

# Example usage:
s1 = "hello"
print(score_of_string(s1))  # Output: 13

s2 = "zaz"
print(score_of_string(s2))  # Output: 50
