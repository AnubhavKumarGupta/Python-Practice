n = "RJIQZMJCIMSNDBOHBRAWIENODSALETAKGKPYUFGVEFGCBRENZGAdkcetqjljtmttlonpekcovdzebzdkzggwfsxhapmjkdbuceak"
u = []
l = []
for i in n:
    if ord(i) > 65 and ord(i) < 97:
        u.append(i)
    else:
        l.append(i)

a = str(u)
b = str(l)

if len(u) > len(l):
    print(n.upper())
else:
    print(n.lower())
