n,m=map(int,input().split())
mat=[[int(i) for i in input().split()] for j in range(n)]
d=[]
f=[]
g=0
s=0
for i in range(0,len(mat)):
    if i%2:
        d.append(mat[i])
    else:
        f.append(mat[i])
for i in d:
    for j in i:
        g+=j
for i in f:
    for j in i:
        s+=j
print(s,g)
    