def solve(n,a):
    a.sort()
    max_2=a[-1]*a[-2]
    max_3=a[-1]*a[-2]*a[-3]
    
    max_1=a[-1]*a[1]*a[0]

    return max(max_1,max_2,max_3)
if __name__=='__main__':
    n=int(input())
    a=list(map(int,input().split()))
    print(solve(n,a))