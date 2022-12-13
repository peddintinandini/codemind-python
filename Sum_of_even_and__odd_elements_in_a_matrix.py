n,m=map(int,input().split())
mat=[[int(i) for i in input().split()] for j in range(n)]
d=[]
f=[]
for i in mat:
    for j in i:
        if j%2==0:
            d.append(j)
        else:
            f.append(j)
print(sum(d),sum(f))