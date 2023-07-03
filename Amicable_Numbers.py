n=int(input())
m=int(input())
sum=0
sum1=0
for i in range(1,n):
    if n%i==0:
        sum+=i
for i in range(1,m):
    if m%i==0:
        sum1+=i
if sum==m and sum1==n:
    print("Amicable")
else:
    print("Not Amicable")