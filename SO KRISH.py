def giaithua(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result
def solve(n):
    tong=0
    for i in str(n):
        tong+=giaithua(int(i))
    return n==tong
if __name__=='__main__':
    n=int(input())
    for _ in range(n):
        num=int(input())
        print('Yes') if solve(num) else print('No')