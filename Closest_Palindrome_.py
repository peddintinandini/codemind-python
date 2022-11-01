def reverse(n):
    rev=0
    temp=n
    while n:
        r=n%10
        rev=rev*10+r
        n=n//10
    if rev==temp:
        return True
    else:
        return False
    

a=int(input())
temp=a
for i in range(a-1,0,-1):
    if reverse(i)==True:
        e=i
        break
a=a+1
while a:
    if reverse(a)==True:
        h=a
        break
    a=a+1

g=abs(temp-e)
l=abs(temp-h)
if g>l:
    print(h)
elif g<l:
    print(e)
else:
    print(e,h)
    
        

   