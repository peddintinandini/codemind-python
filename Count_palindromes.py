def pal(n):
    rev=0
    temp=n
    while n:
        r=n%10
        rev=rev*10+r
        n=n//10
    if temp==rev:
        return True
    else:
        return False
n=int(input())
d=list(map(int,input().split()))
c=0
for i in d:
    if pal(i):
        c+=1
print(c)
