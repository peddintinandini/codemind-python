n=int(input())
x=list(map(int,input().split()))
c=0
a=0
for i in range(n):
    a+=x[i]
h=a//n
for i in range (n):
    if x[i]>=h:
        c+=1
print(c)