def solve(n):
    for i in range(1000):
        if n%7==0:
            return n
        palind_n=int(str(n)[::-1])
        n+=palind_n
    return -1
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        print(solve(n))