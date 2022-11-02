n=int(input())
for i in range(n):
    n,m=(map(int,input().split()))
    for j in range(m):
        if (j*j)%m==n:
            print(j)
            break
    else:
        print("-1")