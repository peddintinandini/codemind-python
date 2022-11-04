n=int(input())
x=list(map(int,input().split()))
b=n-1
h=0
for i in range(n):
    h+=x[i]*(2**b)
    b-=1
print(h)