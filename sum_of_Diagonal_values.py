n,m=map(int,input().split())
a=[]
for i in range(n):
    l=list(map(int,input().split()))
    a.append(l)
n=len(a)
s=0
for i in range(n):
    s+=a[i][i]
    s+=a[i][n-1-i]
if n%2!=0:
    s-=a[n//2][n//2]
print(s)