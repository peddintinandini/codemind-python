def pal(n):
    temp=n
    rev=0
    while n:
        r=n%10
        rev=rev*10+r
        n=n//10
    if temp==rev:
        return True
    else:
        return False
n=int(input())
m=int(input())
for i in range(n,m+1):
    if pal(i):
        print(i,end=" ")