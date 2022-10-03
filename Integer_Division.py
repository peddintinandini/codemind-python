a=int(input())
if a>=0:
    c=a//10
    print(c)
elif a<0:
    if a%10==0:
        print(a//10)
    elif a%10!=0:
        d=int(a/10)-1
        print(d)
else:
    print("0")