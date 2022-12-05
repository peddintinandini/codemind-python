n=int(input())
d=list(map(int,input().split()))
s=len(d)-1
c=0
for i in range(len(d)-1):
    if d[i+1]>d[i]:
        c+=1
if c==s:
    print("yes")
else:
    print("no")