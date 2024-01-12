def isPalind(n):
    if (n<=10):
        return False
    temp=n
    rev=0
    while n>0:
        rev=rev*10+n%10
        n//=10
    if temp==rev:
        return True
    else:
        return False
def solve(n,m,a):
    max_val=float('-inf')
    for i in range(n):
        for j in range(m):
            if isPalind(a[i][j]):
                max_val=max(max_val,a[i][j])
    check=False
    temp=[]
    for i in range(n):
        for j in range(m):
            if a[i][j]==max_val:
                temp.append(f'Vi tri [{i}][{j}]')
                check=True
    if check==False:
        print('NOT FOUND')
    else:
        print(max_val)
        for i in temp:
            print(i)
        print()
if __name__=='__main__':
    n,m=map(int,input().split())
    a=[]
    for i in range(n):
        b=list(map(int,input().split()))
        a.append(b)
    solve(n,m,a)