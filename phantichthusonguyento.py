from math import *
def phantich(n):
    if n!=1:
        print('1 * ',end='')
    else:
        print(1)
    for i in range(2,isqrt(n)+1):
        mu=0
        if n%i==0:
            while n%i==0:
                mu+=1
                n//=i
            print(i,mu,sep='^',end='')
            if n!=1:
                print(' * ',end='')
    if n>1:
        print(n,1,sep='^')
if __name__=='__main__':
    n=int(input())
    for _ in range(n):
        num=int(input())
        phantich(num)