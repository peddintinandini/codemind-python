n=int(input())
l=list(map(int,input().split()))
i=0
j=n-1
if n%2==0:
    while j>i:
        print(l[i],l[j],end=' ')
        i+=1
        j-=1
else:
    while j>i:
        print(l[i],l[j],end=' ')
        i+=1
        j-=1
    print(l[n//2],'0')
        