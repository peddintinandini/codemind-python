def coun(n):
    if n==0:
        return 1
    m=0
    if n<0:
        n=abs(n)
    while n>0:
        r=n%10
        m+=1
        n=n//10
    return m

n,m=map(int,input().split())
d=list(map(int,input().split()))
k=0
for i in d:
    if coun(i)==m:
        k+=1
print(k)
