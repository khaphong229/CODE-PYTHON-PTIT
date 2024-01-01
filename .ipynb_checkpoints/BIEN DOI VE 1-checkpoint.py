def solve(n):
    cnt=0
    if n==1:
        return 1
    while n!=1:
        if n%2==0:
            n/=2
            cnt+=1
        else:
            n=n*3+1
            cnt+=1
    return cnt+1
if __name__=='__main__':
    while 1:
        num=int(input())
        if num==0:
            break
        print(solve(num))
        