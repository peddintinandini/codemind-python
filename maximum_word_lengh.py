n=input()
d=n.split()
a=[]
for i in d:
    a.append(len(i))
print(max(a))