n,m=map(int,input().split())
a=[]

for i in range(n):
    l=list(map(int,input().split()))
    a.append(l)
c=0
for i in range(n):
     if a[i] ==sorted(a[i]) or a[i]==sorted(a[i] ,reverse= True):
        c+=1
print(c)