n=int(input())
for i in range(n+1):
    s=input()
    c=0
    for i in s:
        if i.isdigit():
            c=1
    if c==1:
        print("Yes")
    else:
        print("No")