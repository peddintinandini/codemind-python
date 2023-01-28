a=input()
b=input()
v=a.lower()
h=b.lower()
n=v.split(" ")
m=h.split(" ")
c=0
for i in n:
    for j in m:
        if i==j:
            c+=1
print(c)