def prime(n):
    c=0
    if n==1:
        return False
    for i in range (2,(n//2+1)):
        if n%i==0:
            c+=1
    if c==0:
        return True
    else:
        return False
n=int(input())
h=prime(n)
if prime(n):
    print("prime")
else:
    print("not a prime")