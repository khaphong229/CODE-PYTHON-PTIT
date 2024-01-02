from math import *
def nt(n):
    if n<2:
        return False
    for i in range(2,isqrt(n)+1):
        if n%i==0:
            return False
    return True

n,m=map(int,input().split())
a=[]
for _ in range(n):
    b=list(map(int,input().split()))
    a.append(b)
max_val=-10**18
for i in range(n):
    for j in range(m):
        if nt(a[i][j]):
            max_val=max(max_val,a[i][j])
if max_val!=-10**18:
    print(max_val)
    for i in range(n):
        for j in range(m):
            if a[i][j]==max_val:
                print(f'Vi tri [{i}][{j}]')
else:
    print('NOT FOUND')