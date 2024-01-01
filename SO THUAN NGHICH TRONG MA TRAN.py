def isPalind(n):
    if str(n)==str(n)[::-1]:
        return True
    return False
def solve(n,m,a):
    max_val=float('-inf')
    for i in range(n):
        for j in range(m):
            if isPalind(a[i][j]):
                max_val=max(max_val,a[i][j])
    return max_val
if __name__=='__main__':
    n,m=map(int,input().split())
    a=[]
    for i in range(n):
        b=list(map(int,input().split()))
        a.append(b)
    result=solve(n,m,a)
    if result==float('-inf'):
        print('NOT FOUND')
    else:
        print(result)
        for i in range(n):
            for j in range(m):
                if a[i][j]==result:
                    print(f'Vi tri [{i}][{j}]')