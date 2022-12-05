n=int(input())
d=list(map(int,input().split()))
a,b=map(int,input().split())
m=[]
for i in d:
    if a<=i and b>=i:
        m.append(i)
if len(m)==0:
    print("-1")
else:
    print(min(m))

