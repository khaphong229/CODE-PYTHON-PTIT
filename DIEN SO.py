def dienSo(n,a):
    d=dict({})
    for x in a:
        if x in d: d[x]+=1
        else: d[x]=1
    max_val=max(a)
    min_val=min(a)
    cnt=0
    for i in range(min_val,max_val+1,1):
        if i not in d:
            cnt+=1
    return cnt
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    print(dienSo(n,a))