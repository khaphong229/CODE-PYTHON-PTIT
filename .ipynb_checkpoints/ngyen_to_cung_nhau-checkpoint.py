def ucln(a,b):
    while b!=0:
        a,b=b,a%b
    return a==1

def solve(n,a):
    a.sort()
    for i in range(n-1):
        for j in range(i+1,n):
            if ucln(a[i],a[j]):
                print(a[i],a[j])

if __name__=='__main__':
    n=int(input())
    a=list(map(int, input().split()))
    solve(n,a)