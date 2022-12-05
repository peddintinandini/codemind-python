n=int(input())
d=list(map(int,input().split()))
m=[]
for i in d:
    if i==d.count(i):
        m.append(i)
s=set(m)
if len(s)==0:
    print("-1")
else:
    a=sum(s)/len(s)
    print('%.2f'%a)