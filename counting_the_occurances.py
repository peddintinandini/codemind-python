n=input()
c=input()
l=0
for i in n:
    if c==i:
        l+=1
if l==0:
    print("-1")
else:
    print(l)