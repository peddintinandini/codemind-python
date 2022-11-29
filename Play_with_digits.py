def nan(n):
    sum=0
    while n:
        r=n%10
        sum=sum+r
        n=n//10
    return sum
n=int(input())
k=list(map(int,input().split()))
sum=0
for i in k:
    sum=sum+nan(i)
print(sum)
    