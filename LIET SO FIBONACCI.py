f=[0]*93
f[0]=1
f[1]=1
for i in range(2,93):
    f[i]=f[i-1]+f[i-2]

n=int(input())
for _ in range(n):
    a,b=map(int,input().split())
    for i in range(a-1,b):
        print(f[i],end=' ')
    print()