def num(n):
    c=0
    while n:
        r=n%10
        c+=1
        n=n//10
    return c
n=int(input())
temp=n
sum=0
b=num(n)
while b:
     d=n%10
     sum=sum+d**b
     n=n//10
     b=b-1
if temp==sum:
   print("True")
else:
    print("False")
