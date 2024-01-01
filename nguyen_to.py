from math import *
def ucln(a,b):
    while b!=0:
        a,b=b,a%b
    return a
def prime(n):
    if n<2: return False
    for i in range(2,isqrt(n)+1):
        if n%i==0:
            return False
    return True
def count_prime(n):
    cnt=0
    for i in range(1,n):
        if ucln(i,n)==1:
            cnt+=1
    return cnt

n=int(input())
for _ in range(n):
    num=int(input())
    print('YES') if prime(count_prime(num)) else print('NO')