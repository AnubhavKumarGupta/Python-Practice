n1 = int(input())
n2 = int(input())

def prime(n1, n2):
    l = []
    for i in range(n1, n2+1):
        if i > 1:
            for j in range(2,i):
                if i%j ==0:
                    break
            else:
                l.append(i)
    print(l)
                
print(prime(n1,n2))