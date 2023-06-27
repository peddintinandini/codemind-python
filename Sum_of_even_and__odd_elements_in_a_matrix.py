a,b=map(int,input().split())
m=[]
e=[]
o=[]
for i in range(a):
    l=list(map(int,input().split()))
    m.append(l)
    for j in l:
        if (j%2==0):
            e.append(j)
        else:
            o.append(j)
print(sum(e),sum(o))
            
    