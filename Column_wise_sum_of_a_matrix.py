n,m=map(int,input().split())
mat=[[int(i) for i in input().split()] for j in range(n)]
h=[]
v=list(zip(*mat))
for i in v:
    m=sum(i)
    h.append(m)
print(*h)