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

n=int(input())
d=list(map(int,input().split()))
s=[]
k=0
for i in d:
    s.append(coun(i))
for i in d:
    if max(s)==coun(i):
        print(i,end=" ")
