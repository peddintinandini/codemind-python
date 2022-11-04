n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
sum=0
for i in range(n):
    if a[i]<b or a[i]>c:
        sum=sum+a[i]
print(sum)