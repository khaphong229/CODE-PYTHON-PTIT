def total(n):
    total=0
    while n!=0:
        total+=n%10
        n//=10
    return total
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        a.sort()
        a.sort(key=total)
        print(*a)
            