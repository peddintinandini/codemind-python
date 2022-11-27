from math import sqrt
def sqrn(n):
    v=int(sqrt(n))
    return (v*v)==n
for i in range(int(input())):
    n=int(input())
    if sqrn(n)==True:
        print("True")
    else:
        print("False")