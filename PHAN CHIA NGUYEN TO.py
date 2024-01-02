from math import *
def nt(n):
    if n<2:
        return False
    for i in range(2,isqrt(n)+1):
        if n%i==0:
            return False
    return True

n=int(input())
a=list(map(int,input().split()))
b=[]
for x in a:
    if x not in b:
        b.append(x)
m=len(b)

def check(b,m):
    for i in range(0,m):
        if nt(sum(b[0:i+1])) and nt(sum(b[i+1:m])):
              return i
    return 'NOT FOUND'

print(check(b,m))