def rev(n):
    rev=0
    temp=n
    while n:
        r=n%10
        rev=rev*10+r
        n= n//10
    return rev
n=int(input())
d=list(map(int,input().split()))
for i in d:
    if rev(i):
        print(rev(i),end=" ")