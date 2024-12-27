def minimumChairs(s):
    e =[]
    ce = 0
    l = []
    le = 0
    for i in range(len(s)):
        if s[i] =="E":
            ce = ce + 1
            e.append(ce)
        else:
            ce = ce - 1
            e.append(le)
    return max(e)


s = "ELEELEELLL"
print(minimumChairs(s))