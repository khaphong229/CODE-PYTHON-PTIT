from collections import Counter
def odd_fre(n,a):
    b=dict(Counter(a))
    for i in b:
        if b[i]%2==1:
            return i
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        print(odd_fre(n,a))