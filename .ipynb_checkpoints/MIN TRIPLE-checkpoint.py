def min_triple(n,a):
    if n<3:
        return 0
    min1=10*18
    min2=10*18

    for i in a:
        if i<min1:
            min2=min1
            min1=i
        elif i<min2:
            min2=i
    return min1+min2+min(a)

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    print(min_triple(n,a))