from math import *
def number_of_divisors(n):
    cnt=0
    for i in range(1,isqrt(n)+1):
        if n%i==0:
            cnt+=1
            if i!=n//i:
                cnt+=1
    return cnt

def check_anti_prime(n):
    number_of_divisors_of_n=number_of_divisors(n)
    for i in range(1,n):
        if number_of_divisors(i)>=number_of_divisors_of_n:
            return False
    return True
def check(x):
    i=1
    while True:
        if i>x:
            if check_anti_prime(i):
                return i
        i+=1
if __name__=='__main__':
    n=int(input())
    for _ in range(n):
        num=int(input())
        print(check(num))