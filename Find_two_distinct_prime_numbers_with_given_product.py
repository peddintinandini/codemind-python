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
temp=n
for i in range(2,n+1):
    if n%i==0:
         b=n//i
         if prime(i) and prime(b):
            print(i,b)
            break
else:
    print("-1")