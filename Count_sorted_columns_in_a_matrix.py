n,m=map(int,input().split())
a=[]

for i in range(n):
    l=list(map(int,input().split()))
    a.append(l)
c=0
s=[]
for i in range(m):
    d=[]
    for j in range(n):
        d.append(a[j][i])
    s.append(d)
for i in s:
    if i == sorted(i):
        c+=1
print(c)
