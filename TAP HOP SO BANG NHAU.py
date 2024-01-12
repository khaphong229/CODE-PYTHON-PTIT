def check_equal(a,b):
    if len(a)!=len(b):
        return False
    for i in range(len(a)):
        if a[i]!=b[i]:
            return False
    return True
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
# n,m=12,18
# a=[1, 2, 3, 4, 5, 1, 2, 3, 5, 4, 1, 2]
# b=[1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 5, 5, 5, 5, 5, 5]
A,B=sorted(list(set(a))),sorted(list(set(b)))
print('YES') if check_equal(A,B) else print('NO')