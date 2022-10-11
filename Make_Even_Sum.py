n=int(input())
arr=list(map(int,input().split()))
sum=0
for i in range (0,n,1):
    if n%2==0:
        sum=sum+arr[i]
if sum%2==0:
    print("1")
else:
    print("0")