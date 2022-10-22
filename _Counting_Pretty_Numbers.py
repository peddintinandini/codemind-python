for _ in range (int(input())):
    a,b=map(int,input().split())
    c=0
    for i in range(a,b+1,1):
        r=i%10
        if r==2 or r==3 or r==5:
            c=c+1
    print(c)
    
        