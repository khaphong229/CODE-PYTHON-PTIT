def dem(n):
    cnt=0
    if n<=9: return 1
    while n>=10:
        sum=0
        while n>0:
            sum+=n%10
            n//=10
        n=sum
        cnt+=1
    return cnt

if __name__=='__main__':
    n=int(input())
    print(dem(n))