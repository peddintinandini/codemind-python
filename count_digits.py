n=int(input())
a=list(map(int,input().split()))
for i in a:
    m=i
    if i<0:
        i=abs(i)
    c=0
    if m==0:
        c=1
    while i>0:
        r=i%10
        c+=1
        i=i//10
    print(c,end=" ")

