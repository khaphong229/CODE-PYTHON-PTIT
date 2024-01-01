def ucln(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def khoang(k):
    start=10**(k-1)
    end=10**k-1
    return range(start,end+1)

n,k=map(int,input().split())
cnt=-1
for i in khoang(k):
    if ucln(n,i)==1:
        cnt+=1
        if cnt==10:
            print()
            cnt=0
        print(i,end=' ')