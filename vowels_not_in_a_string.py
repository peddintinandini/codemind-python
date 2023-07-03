n=input()
v='aeiou'
d=''
for i in v:
    if i not in n:
        d+=i
if len(d):
    for i in d:
        print(i,end=' ')
else:
    print("0")