n=int(input())
d=list(map(int,input().split()))
a=[]
b=[]
for i in range (len(d)):
    if i%2==0:
        a.append(d[i])
        
    else:
        b.append(d[i])
        
for i in range(len(a)):
    for j in range(len(b)):
        if i==j:
            
            for k in range(1,b[j]+1):
                print(a[i],end=" ")