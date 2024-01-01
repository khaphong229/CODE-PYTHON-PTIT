import math
def check_even(n):
    for x in range(2,len(str(n))+1,2):
        if int(str(n)[x])%2==0:
            return True
    return False

def check_odd(n):
    for x in range(1,len(str(n))+1,2):
        if int(str(n)[x])%2==1:
            return True
    return False

def total(n):
    total=0
    for x in str(n):
        total+=int(x)
    return total

def prime(n):
    if n<2: return False
    for i in range(2,math.isqrt(n)+1):
        if n%i==0:
            return False
    return True

if __name__=='__main__':
    n=int(input())
    for _ in range(n):
        num=int(input())
        if check_even(num) and check_odd(num) and prime(total(num)):
            print('YES')
        else:
            print('NO')