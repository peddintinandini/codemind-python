def prime(n):
    c=0
    for i in range(2,(n//2+1)):
        if n%i==0:
            c+=1
    if c==0:
        return True
    else:
        return False
def rev(n):
    reve=0
    while n:
        r=n%10
        reve=reve*10+r
        n=n//10
    return reve

n=int(input())
if prime(n):
    if prime(rev(n)):
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")


      

