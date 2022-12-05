s=int(input())
for i in range(s+1):
    n=input()
    c=0
    for i in n:
        if i.isdigit():
            c+=1
    if c==len(n):
        print("True")
    else:
        print("False")