def solve(n,a):
    max_val=max(a)
    min_val=min(a)
    while min_val in a:
        a.remove(min_val)
    while max_val in a:
        a.remove(max_val)
    tong=0
    for i in a:
        tong+=i
    return round((tong/len(a)),2)
n=int(input())
a=list(map(float,input().split()))
print(solve(n,a))