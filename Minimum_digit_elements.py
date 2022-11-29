def con(n):
    c=0
    while n:
        r=n%10
        c+=1
        n=n//10
    return c
n=int(input())
k=list(map(int,input().split()))
c=99999
e=0
for i in range(n):
    if con(k[i])<c:
        c=con(k[i])
for i in range(n):
    if con(k[i])==c:
        e+=1
print(e)