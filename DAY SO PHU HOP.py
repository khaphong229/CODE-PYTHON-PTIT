def phuHop(a,b):
    a.sort()
    b.sort()

    for i in range(len(a)):
        if a[i]>b[i]:
            return False
    return True

if __name__=='__main__':
    slTest=int(input())
    for _ in range(slTest):
        phTu=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        print('YES') if phuHop(a,b) else print('NO')
