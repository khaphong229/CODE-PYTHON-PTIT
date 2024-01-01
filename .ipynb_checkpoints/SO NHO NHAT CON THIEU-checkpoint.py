def solve(n,a):
    a.sort()
    for i, num in enumerate(a):
        if num!=i+1:
            return i+1
    return n

n=int(input())
a=list(map(int,input().split()))
print(solve(n,a))
        