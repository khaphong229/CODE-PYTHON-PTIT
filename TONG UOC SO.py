from math import *
prime=[True] * (2*10**6+1)
def sieve():
    prime[0], prime[1]=False, False
    for i in range(2,isqrt(2*10**6+1)+1):
        if prime[i]:
            for j in range(i**2,2*10**6+1,i):
                prime[j]=False
if __name__=='__main__':
    sieve()
    t=int(input())
    tong=0
    for i in range(t):
        sum=0
        n=int(input())
        for i in range(50):
            if prime[i] and n%i==0:
                    while n%i==0:
                        sum+=i
                        n//=i
        tong+=sum
    print(tong)