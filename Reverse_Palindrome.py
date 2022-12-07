def rev(n):
    s=0
    while n:
        r=n%10
        s=s*10+r
        n=n//10
    return s
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
while True:
    n=n+rev(n)
    if pal(n):
        print(n)
        break