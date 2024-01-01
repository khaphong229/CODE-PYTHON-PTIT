from math import *
def dem_uoc(n):
    cnt=0
    for i in range(1,isqrt(n)+1):
        if n%i==0:
            cnt+=2 if i!=n//i else 1
    return cnt==9
        
if __name__=='__main__':
    n=int(input())
    cnt=0
    for i in range(1,n+1):
        if dem_uoc(i):
            cnt+=1
    print(cnt)