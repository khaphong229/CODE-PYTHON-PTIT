def count_couple_dif(n,a):
    cnt=0
    for i in range(n-1):
        if a[i]!=a[i+1]:
            cnt+=1
    return cnt

n=int(input())
a=[int(i) for i in input().split()]
print(count_couple_dif(n,a))