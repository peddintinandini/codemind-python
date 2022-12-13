n,m=map(int,input().split())
mat=[[int(i) for i in input().split()] for j in range(n)]
d=[]

for i in mat:
    for j in i:
        d.append(j)
print(sum(d))