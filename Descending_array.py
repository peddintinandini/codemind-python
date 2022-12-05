n=int(input())
d=list(map(int,input().split()))
a=[]
for i in d:
    a.append(i)
d.sort()
d.reverse()
if a==d:
    print("yes")
else:
    print("no")