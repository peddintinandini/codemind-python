n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
d=0
for i in range(n):
    if a[i]<b or a[i]>c:
        print(a[i],end=" ")
        d=1
if d==0:
    print("-1")