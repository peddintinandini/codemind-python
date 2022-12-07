def sel(n):
    c=0
    s=0
    t=n
    while n:
        r=n%10
        c+=1
        if r!=0:
            if t%r==0:
                s+=1
        n=n//10
    if c==s:
        return True
    else:
        return False
a=int(input())
b=int(input())
for i in range(a,b+1):
    if sel(i):
        print(i,end=" ")
        