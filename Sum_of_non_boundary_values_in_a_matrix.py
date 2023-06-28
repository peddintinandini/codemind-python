n,m=map(int,input().split())
a=[]
s=0 
s1=0
for i in range(n):
    l=list(map(int,input().split()))
    a.append(l)
    s+=sum(l)
for i in range(n):
    for j in range(m):
        if i==0 or j==0 or i==n-1 or j==m-1:
            s1+=a[i][j]
print(s-s1)
