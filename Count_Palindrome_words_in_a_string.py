n=input()
b=n.lower()
c=0
a=b.split(" ")
for i in a:
    if i==i[::-1]:
        c+=1
print(c)