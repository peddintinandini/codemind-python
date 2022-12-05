n=int(input())
d=list(map(int,input().split()))
m=[]
for i in  d:
    if i==d.count(i):
        m.append(i)
if len(m)==0:
    print("-1")
else: 
    print(min(m),end=" ")
    print(max(m),end=" ")