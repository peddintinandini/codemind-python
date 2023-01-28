n=input()
a=n.split(" ")
for i in range(len(n)):
    if i%2==0:
        a[i]=a[i][::-1]
    print(a[i],end=" ")
