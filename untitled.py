def is_even_palind(n):
    if n!=n[::-1] or len(n)%2==1:
        return False
    for i in n:
        if int(i)%2==1:
            return False
    return True

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        for i in range(22,n,2):
            if is_even_palind(i):
                print(i,end=' ')
        print()