def prime(n):
    c=0
    if n==1:
        return False
    for i in range(2,(n//2+1)):
        if n%i==0:
            c+=1
    if c==0:
        return True
    else:
        return False
    
n=int(input())
for _ in range(n):
    n=int(input())
    temp=n
    for i in range(n-1,0,-1):
        if prime(i):
            l=i
            break
    for j in range(n,99999,1):
        if prime(j):
            h=j
            break
    p=abs(n-l)
    k=abs(n-h)
    if p>k:
        print(h)
    elif p==k:
        print(l)
    else:
        print(l)
            
    
