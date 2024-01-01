from math import *

def nt(n):
    if n<2:
        return False
    for i in range(2,isqrt(n)+1):
        if n%i==0:
            return False
    return True

def ds_nt(n):
    f=[]
    num=2
    while len(f)<n:
        if nt(num):
            f.append(num)
        num+=1
    return f
    
def solve(n,x):
    list_nt=ds_nt(n)
    kq=[x]
    for i in list_nt:
        x+=i
        kq.append(x)
    return kq

if __name__=='__main__':
    n,x=map(int,input().split())
    print(*solve(n,x))