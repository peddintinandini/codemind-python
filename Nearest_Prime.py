def prime(n):
    c=0
    if n==1:
        return False
    for i in range(2,int((n**(0.5))+1)):
        if n%i==0:
            c+=1
    if c==0:
        return True
    else:
        return False
for i in range(int(input())):
    n=int(input())
    for i in range(n,2,-1):
        if prime(i):
            b=i
            break
    for i in range(n+1,9999,1):
        if prime(i):
            c=i
            break
    g=abs(n-b)
    h=abs(n-c)
    if g>h:
        print(c)
    elif g<=h:
        print(b)
    
    
