n,m=map(int,input().split())
k=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
d=[]
for i in k:
    for j in b:
        if i not in c:
            if i==j:
               c.append(i)

print(*c)