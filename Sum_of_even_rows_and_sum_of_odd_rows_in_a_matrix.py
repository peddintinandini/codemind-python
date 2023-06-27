a,b=map(int,input().split())
m=[]
s1=0
s2=0
for i in range(a):
    l=list(map(int,input().split()))
    m.append(l)
    if (i%2==0):
        s1+=sum(l)
    else:
        s2+=sum(l)
print(s1,s2)
            
    