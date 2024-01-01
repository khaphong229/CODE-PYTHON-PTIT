def solve(a):
    min_val=float('inf')
    max_val=float('-inf')
    for i in a:
        min_val=min(min_val,i)
        max_val=max(max_val,i)
    return min_val,max_val
while 1:
    n=int(input())
    if n==0:
        break
    a=[]
    for i in range(n):
        num=int(input())
        a.append(num)
    nho,lon=solve(a)
    if nho==lon:
        print('BANG NHAU')
    else:
        print(nho,lon)