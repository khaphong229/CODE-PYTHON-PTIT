n=int(input())
a=[]
for i in range(n):
    a.append([int(j) for j in input().split()])
res=[]
res.append(int((a[0][1]+a[0][2]-a[1][2])/2))
for i in range(1,n):
    res.append(a[0][i]-res[0])
for i in res:
    print(i,end=' ')