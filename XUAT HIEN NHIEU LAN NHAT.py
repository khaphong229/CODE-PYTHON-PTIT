from collections import Counter
def max_fre(n,a):
    max_val=-10**18
    b=dict(Counter(a))
    for i in b:
        max_val=max(max_val,b[i])
    for i in b:
        if b[i]==max_val:
            return i,max_val

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    so,tan_suat=max_fre(n,a)
    if tan_suat > n/2:
        print(so)
    else:
        print('NO')
    