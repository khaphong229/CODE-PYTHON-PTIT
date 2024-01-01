from math import *
def is_prime(n):
    if n<2:
        return False
    for i in range(2,isqrt(n)+1):
        if n%i==0:
            return False
    return True

def check_location(n):
    for i in str(n):
        if is_prime(int(i))!=is_prime(int(str(n).index(i))):
            return False
    return True

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n=input()
        print('YES') if check_location(n) else print('NO')