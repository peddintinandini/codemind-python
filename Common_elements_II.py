n,m=map(int,input().split())
k=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
d=[]
for i in k:
    for j in b:
        if i==j:
            c.append(j)
for i in k:
    if i not in c:
          if i not in d:
            d.append(i)
for j in b:
    if j not in c:
        if j not in d:
            d.append(j)
print(*d)