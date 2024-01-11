from math import *

prime=[True]*(10**6+1)
prime[0]=prime[1]=False
for i in range(2,isqrt(10**6)+1):
    if prime[i]:
        for j in range(i*i,10**6+1,i):
            prime[j]=False

for case in range(int(input())):
    cnt=0
    for i in range(int(input())-5):
        if prime[i] and prime[i+6]:
            if prime[i+2] or prime[i+4]:
                cnt+=1
    print(cnt)