n=input()
v1='aeiou'
v2='AEIOU'
a=''
b=''
for i in v1:
    if i in n:
        a+=i
for i in v2:
    if i in n:
        b+=i
if a==v1 or b==v2:
    print("True")
else:
    print("False")