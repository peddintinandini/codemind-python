def prime(n):
    c=0
    if n==1:
        return True
    for i in range (2,(n//2)+1):
        if n%i==0:
            c+=1
    if c==0:
        return False
    else :
        return True
n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0:
        if prime(i):
            c+=1
print(c)