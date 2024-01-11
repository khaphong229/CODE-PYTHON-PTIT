n=int(input())
a=[]
for _ in range(n):
    b=[str(i) for i in input()]
    a.append(b)
cnt=0
for i in range(n):
    for j in range(n-1):
        if a[i][j]==a[i][j+1]=='C':
            cnt+=1
        if a[j][i]==a[j+1][i]=='C':
            cnt+=1

print(cnt)