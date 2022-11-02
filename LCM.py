a,b=map(int,input().split())
m=a
g=b
while b!=0:
    a,b=b,a
    b=b%a
n=a
print((m*g)//n)
    