#declare library
from math import *
#a
n=int(input())
#b
a=[]
for i in range(n):
    t=int(input())
    a.append(t)
print()
b=sorted(a)
print(b)
print()
#c
tong=0
tich=1
for i in b:
    tong+=i
    tich*=i
print('YES') if tich>tong else print('NO')
print()
#d
def nt(n):
    if n<2:
        return False
    for i in range(2,isqrt(n)+1):
        if n%i==0:
            return False
    return True
cnt=0
for i in b:
    if nt(i):
        cnt+=1
print(cnt)
print()
#e
def tong_chu_so(n):
    if n<10:
        return n
    tong=0
    while n!=0:
        tong+=n%10
        n//=10
    return tong
dem=0
for i in b:
    if nt(tong_chu_so(i)):
        dem+=1
print(dem)