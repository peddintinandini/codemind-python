s=input()
v="AEIOUaeiou"
c=[]
for i in s:
    if i in v:
        if i not in c:
            c.append(i)
if len(c)==0:
    print("-1")
else:
    print(*c)