def prime(n):
    c=0
    if n==1:
        return False
    for i in range (2,(n//2+1)):
        if n%i==0:
            c+=1
    if c==0:
        return True
    else:
        return False
n=int(input())

if prime(n):
    while n:
       r=n%10
       n=n//10
       if r==1 or r==4 or r==6 or r==8 or r==9:
           print("Not Mega Prime")
           break
    else:
        print("Mega Prime")
        
else:
    print("Not Mega Prime")