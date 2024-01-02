from itertools import combinations
def solve(n,d):
    cnt=0
    b=list(combinations(d,3))
    for i in b:
        if sum(i)==0:
            cnt+=1
    return cnt
t=int(input())
for _ in range(t):
    n=int(input())
    d=list(map(int,input().split()))
    print(solve(n,d))