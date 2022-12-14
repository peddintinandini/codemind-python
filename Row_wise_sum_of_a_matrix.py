n,m=map(int,input().split())
mat=[[int(i) for i in input().split()] for j in range(n)]
h=[]

for i in mat:
    m=sum(i)
    h.append(m)
print(*h)