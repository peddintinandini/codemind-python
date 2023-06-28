def pal(s):
    if s == s[::-1]:
        return True
    else:
        return False

s=input().lower()
s=s.split()
c=0
for i in s:
    if pal(i)== True:
        c+=1
print(c)
