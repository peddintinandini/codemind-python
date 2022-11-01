def prime(n):
    c=0
    if n==1:
        return False
    for i  in range(2,(n//2+1)):
        if n%i==0:
            c+=1
    if c==0:
        return True
    else:
        return False
a=int(input())
b=int(input())
h=a+b
k=1
while True:
    if prime(h+k):
        print(k)
        break
    k+=1
    
        