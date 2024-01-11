for _ in range(int(input())):
    n,index=map(int,input().split())
    a=list(map(int,input().split()))
    print(*(a[index:]+a[:index]))