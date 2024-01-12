def so_dep(n,m,a):
    max_val=-10**18
    min_val=10**18
    for i in a:
        max_val=max(max_val,max(i))
        min_val=min(min_val,min(i))
    soDep=max_val-min_val

    check=False
    temp=[]

    for i in range(n):
        for j in range(m):
            if a[i][j]==soDep:
                temp.append(f'Vi tri [{i}][{j}]')
                check=True
    if check==True:
        print(soDep)
        for i in temp:
            print(i)
    else:
        print('NOT FOUND')


if __name__=='__main__':
    n,m=map(int,input().split())
    a=[]
    for i in range(n):
        b=list(map(int,input().split()))
        a.append(b)
    so_dep(n, m, a)