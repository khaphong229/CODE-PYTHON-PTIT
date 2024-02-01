from math import *

def prime(n):
    if n<2: return False
    for i in range(2,isqrt(n)+1):
        if n%i==0: return False
    return True

def solve(n,a):
    primes=[x for x in a if prime(x)]
    primes.sort()

    result=[]
    primeIndex=0
    for i in a:
        if prime(i):
            result.append(primes[primeIndex])
            primeIndex+=1
        else:
            result.append(i)
    return result



if __name__=='__main__':
    t=int(input())
    a=list(map(int,input().split()))
    kq=solve(t,a)
    print(*kq)