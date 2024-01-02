import math
def prime(n):
    if n<2: return False
    for i in range(2,math.isqrt(n)+1):
        if n%i==0:
            return False
    return True
def count_num(n):
    cnt=0
    while n!=0:
        cnt+=1
        n//=10
    return cnt
def check_cnt(n):
    cnt_nt=0
    cnt_notnt=0
    for x in str(n):
        if prime(int(x)):
            cnt_nt+=1
        else:
            cnt_notnt+=1
    return cnt_nt>cnt_notnt

if __name__=='__main__':
    n=int(input())
    for _ in range(n):
        num=int(input())
        if prime(count_num(num)) and check_cnt(num):
            print('YES')
        else:
            print('NO')