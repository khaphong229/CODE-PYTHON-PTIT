def solve(n,a):
    chan=[n for n in a if n%2==0]
    le=[n for n in a if n%2==1]
    

    chan.sort()
    #sắp xếp giảm dần key,reverse trong sort
    le.sort(reverse=True)

    kq=[0]*n
    gtri_chan, gtri_le=0,0

    #i là gtri vị trí bắt đầu từ 0
    for i, num in enumerate(a):
        if num%2==0:
            kq[i]=chan[gtri_chan]
            gtri_chan+=1
        else:
            kq[i]=le[gtri_le]
            gtri_le+=1

    return kq

n=int(input())
a=[i for i in input().split()]
print(*solve(n,a))