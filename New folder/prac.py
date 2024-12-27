def convert(list):
    return tuple(list)
def flatten_array(matrix,n,m):
    l=[]
    for i in range(0,n):
        for j in range(0,m):
            l.append(matrix[i][j])
    return l
n,m=list(map(int,input().split()))
matrix=[]
for i in range(0,n):
    a=[]
    matrix.append(list(map(int,input().split())))

matrix2=flatten_array(matrix,n,m)
p=[]
for i in matrix2:
    if matrix2.count(i)==1:
        p.append(i)
answer=convert(p)
if(any(answer)==False):
    print('NO')
else:
    for i in answer:
        print(i,end=" ")