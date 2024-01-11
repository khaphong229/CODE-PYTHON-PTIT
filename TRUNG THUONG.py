def trungThuong():
    d=dict({})
    n=int(input())
    for i in range(n):
        x=int(input())
        if x in d:
            d[x]+=1
        else:
            d[x]=1
    res=float('inf')
    max=1
    for i in d:
        if d[i]>max:
            max=d[i]
    for i in d:
        if d[i]==max:
            res=min(res,int(i))
    print(res)

n=int(input())
for i in range(n):
    trungThuong()