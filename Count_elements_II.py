n,m=map(int,input().split())
k=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
d=[]
for i in k:
    for j in b:
        if i==j:
            c.append(i)
for i in k:
    for j in b:
        if i not in c:
            if i not in d:
                d.append(i)
        if j not in c:
            if j not in d:
                d.append(j)
print(len(d))