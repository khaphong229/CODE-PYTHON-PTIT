def solve(n,a):
    if n<3:
        return 0
    a.sort()
    return a[-1]+a[-2]+a[-3]
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    print(solve(n,a))